import { tool } from "@opencode-ai/plugin"

const MAX_LIMIT = 50
const DEFAULT_LIMIT = 25
const PAGE_STRING_LIMIT = 8000
const DETAIL_STRING_LIMIT = 50000

function unwrap(value) {
  return value && typeof value === "object" && "data" in value ? value.data : value
}

function truncate(value, limit) {
  if (typeof value === "string") {
    if (value.length <= limit) return value
    return `${value.slice(0, limit)}\n...[truncated ${value.length - limit} chars]`
  }
  if (Array.isArray(value)) return value.map((item) => truncate(item, limit))
  if (value && typeof value === "object") {
    const out = {}
    for (const [key, item] of Object.entries(value)) out[key] = truncate(item, limit)
    return out
  }
  return value
}

function sessionSummary(value) {
  return {
    id: value?.id,
    parentID: value?.parentID,
    agent: value?.agent,
    model: value?.model,
    title: value?.title,
    time: value?.time,
    location: value?.location,
    subpath: value?.subpath,
    cost: value?.cost,
    tokens: value?.tokens,
  }
}

async function apiGet(path) {
  const proc = Bun.spawn(["opencode", "api", "GET", path], {
    stdout: "pipe",
    stderr: "pipe",
  })
  const stdoutPromise = new Response(proc.stdout).text()
  const stderrPromise = new Response(proc.stderr).text()
  const code = await proc.exited
  const [stdout, stderr] = await Promise.all([stdoutPromise, stderrPromise])
  if (code !== 0) throw new Error(`opencode api failed (${code}): ${stderr.trim() || stdout.trim()}`)
  try {
    return JSON.parse(stdout)
  } catch {
    throw new Error(`opencode api returned non-JSON output: ${stdout.slice(0, 500)}`)
  }
}

function idString(value) {
  if (typeof value === "string") return value
  if (value && typeof value === "object") {
    if (typeof value.value === "string") return value.value
    if (typeof value.id === "string") return value.id
  }
  return undefined
}

async function sessionInfo(sessionID) {
  return unwrap(await apiGet(`/api/session/${encodeURIComponent(sessionID)}`))
}

async function listChildren(parentID) {
  const items = []
  let cursor
  do {
    const params = new URLSearchParams({ parentID, order: "asc", limit: "100" })
    if (cursor) params.set("cursor", cursor)
    const raw = await apiGet(`/api/session?${params.toString()}`)
    const data = unwrap(raw)
    const page = Array.isArray(data) ? data : raw?.data ?? []
    items.push(...page)
    cursor = raw?.cursor?.next || undefined
  } while (cursor)
  return items
}

async function auditRoot(currentSessionID) {
  const evaluator = await sessionInfo(currentSessionID)
  const parentID = idString(evaluator?.parentID)
  if (!parentID) throw new Error("session-evaluator has no parent session; run it as a child of code-orchestrator")
  const root = await sessionInfo(parentID)
  return { evaluator, root }
}

async function sessionTree(currentSessionID) {
  const { root } = await auditRoot(currentSessionID)
  const rootID = idString(root?.id)
  if (!rootID) throw new Error("parent session ID is unavailable")

  const seen = new Set([currentSessionID])
  const sessions = []
  const excludedEvaluatorIDs = [currentSessionID]
  const queue = [rootID]

  while (queue.length) {
    const parentID = queue.shift()
    for (const child of await listChildren(parentID)) {
      const childID = idString(child?.id)
      if (!childID || seen.has(childID)) continue
      seen.add(childID)
      if (childID === currentSessionID || child?.agent === "session-evaluator") {
        excludedEvaluatorIDs.push(childID)
        continue
      }
      sessions.push(child)
      queue.push(childID)
    }
  }

  return { evaluatorID: currentSessionID, excludedEvaluatorIDs, root, sessions }
}

async function allowedSessionIDs(currentSessionID) {
  const tree = await sessionTree(currentSessionID)
  const ids = new Set()
  const rootID = idString(tree.root?.id)
  if (rootID) ids.add(rootID)
  for (const item of tree.sessions) {
    const id = idString(item?.id)
    if (id) ids.add(id)
  }
  return ids
}

export default tool({
  description: "Read the completed parent OpenCode session tree for post-hoc semantic audit. Use tree first, then page through messages for each participating session; use message only for material truncated detail.",
  args: {
    operation: tool.schema.enum(["tree", "messages", "message"]),
    session_id: tool.schema.string().optional().describe("Session ID from tree; required for messages/message."),
    message_id: tool.schema.string().optional().describe("Message ID; required only for message."),
    cursor: tool.schema.string().optional().describe("Next cursor returned by messages."),
    limit: tool.schema.number().int().min(1).max(MAX_LIMIT).optional().describe(`Messages per page, 1-${MAX_LIMIT}.`),
  },
  async execute(args, context) {
    if (args.operation === "tree") {
      const tree = await sessionTree(context.sessionID)
      return JSON.stringify({
        audited_root: sessionSummary(tree.root),
        participating_children: tree.sessions.map(sessionSummary),
        excluded_evaluator_sessions: tree.excludedEvaluatorIDs,
      }, null, 2)
    }

    if (!args.session_id) throw new Error("session_id is required for messages/message")
    const allowed = await allowedSessionIDs(context.sessionID)
    if (!allowed.has(args.session_id)) throw new Error("session_id is outside this evaluator's parent session tree")

    if (args.operation === "message") {
      if (!args.message_id) throw new Error("message_id is required for message")
      const raw = await apiGet(`/api/session/${encodeURIComponent(args.session_id)}/message/${encodeURIComponent(args.message_id)}`)
      return JSON.stringify(truncate(raw, DETAIL_STRING_LIMIT), null, 2)
    }

    const limit = Math.min(MAX_LIMIT, Math.max(1, args.limit ?? DEFAULT_LIMIT))
    const params = new URLSearchParams({ order: "asc", limit: String(limit) })
    if (args.cursor) params.set("cursor", args.cursor)
    const raw = await apiGet(`/api/session/${encodeURIComponent(args.session_id)}/message?${params.toString()}`)
    return JSON.stringify(truncate(raw, PAGE_STRING_LIMIT), null, 2)
  },
})

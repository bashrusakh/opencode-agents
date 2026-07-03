# Git Branch Provenance Checklist

Use before editing, committing, pushing, opening a PR, or updating an existing PR.

Use explicit refs such as `<base_remote>=origin`, `<base_branch>=main`, `<base_ref>=origin/main`.

```bash
git status -sb
git branch -vv
git remote -v
git fetch --prune <head_remote>
git fetch --prune <base_remote>
git status -sb
git log --oneline --decorate <base_ref>..HEAD
git log --oneline --decorate --left-right --cherry-pick <base_ref>...HEAD
git diff --name-status <base_ref>...HEAD
git diff --stat <base_ref>...HEAD
```

Expected report:

- Base ref
- Current branch
- Upstream tracking branch
- Branch state: current / behind / ahead / diverged / unknown
- Commits ahead of base
- Changed files
- Unrelated commits/files: yes/no
- Safe to edit/commit/push/PR: yes/no

Remember: a PR is the whole base-to-head diff, not just the last commit.

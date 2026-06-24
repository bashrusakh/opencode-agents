# Git Branch Provenance Checklist

Use before editing, committing, pushing, opening a PR, or updating an existing PR.

```bash
git status --short
git branch --show-current
git fetch origin <base>
git log --oneline --decorate --left-right --cherry-pick origin/<base>...HEAD
git diff --name-status origin/<base>...HEAD
git diff --stat origin/<base>...HEAD
```

Expected report:

- Base branch
- Current branch
- Commits ahead of base
- Changed files
- Unrelated commits/files: yes/no
- Safe to edit/commit/push/PR: yes/no

Remember: a PR is the whole base-to-head diff, not just the last commit.

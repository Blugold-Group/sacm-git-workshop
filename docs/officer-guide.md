# Officer guide

How to set this repo up and run the hands-on part of the workshop.

## Before the workshop (about 20 minutes)

1. **Create the repo on GitHub** under the SACM organization (or your own
   account) as a **public** repo named `sacm-git-workshop`, then push this
   folder to it:

   ```bash
   git remote add origin https://github.com/<org>/sacm-git-workshop.git
   git push -u origin main
   ```

   Then replace `YOUR-USERNAME` examples in the README only if you want to;
   they're meant to stay generic.

2. **Allow Actions to run on fork PRs.** Settings → Actions → General →
   "Approval for running fork pull request workflows from contributors".
   First-time contributors need approval by default. Set it to
   **"Require approval for first-time contributors who are new to GitHub"**,
   or be ready to click **Approve and run** on each PR during the workshop.

3. **Protect `main`.** Settings → Rules → Rulesets → New branch ruleset,
   target the default branch, and enable:
   - Restrict deletions
   - Block force pushes
   - Require a pull request before merging (0 approvals is fine, so officers can merge quickly)
   - Require status checks to pass → add **check** (it appears after the workflow has run once)

4. **Add your own member file** through a pull request. This runs the check
   once so you can require it, and it gives students a real example to look at.

5. **Dry run.** Have another officer do the whole student flow from a fork.

6. **Update the slides.** Put the repo URL on the "Your turn" and
   "Questions?" slides.

## During the workshop

- Share the repo URL on screen and in the club chat.
- While students work, officers walk the room. The most common problems:
  - **Authentication fails on push.** Have them run `gh auth login`, or
    create a personal access token and use it as the password.
  - **"Permission denied" on push.** They cloned the SACM repo instead of
    their fork. Fix: `git remote set-url origin https://github.com/THEIR-USERNAME/sacm-git-workshop.git`.
  - **Check fails.** Click **Details** on the PR. The error says exactly what
    to fix. Usually the file name doesn't match the username, or template
    text is left in.
  - **Stuck in Vim.** Press `Esc`, type `:wq`, and press Enter.
- Merge PRs on the projector as they turn green, and read a few fun facts aloud.

### Optional: Live merge conflict demo

Every student adds a different file, so real PRs won't conflict. To show a
conflict on the projector:

```bash
bash exercises/02-merge-conflict/setup.sh
cd playground/merge-conflict
git merge feature/dark-mode
```

Then resolve it in VS Code with the class calling out which side to keep.

## After the workshop

- Leave the repo up. Members can come back to the exercises.
- To reuse it next semester, move the old member files to
  `members/archive/<semester>/` (the check only looks at the top level of `members/`).

## How the check works

`.github/workflows/check-members.yml` runs `scripts/check_members.py` on every
pull request. It uses read-only permissions and the `pull_request` trigger,
so code from forks can't write to the repo or read secrets. The script checks
that each `members/<username>.md` has a real name heading and filled-in
GitHub, Major, Year, and Fun fact lines, and that the GitHub handle matches
the file name. It also warns (without failing) when a PR changes files
outside `members/`.

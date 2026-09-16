# Exercise: Resolve a merge conflict

A merge conflict happens when two branches change the **same lines** of the
same file. Git can't guess which version you want, so it asks you.

## Set up

From the root of the workshop repo:

```bash
bash exercises/02-merge-conflict/setup.sh
```

This creates a separate practice repo in `playground/merge-conflict/`:

- `main` changed `THEME` to `"uwec-blue"` and `MAX_USERS` to `100`
- `feature/dark-mode` changed `THEME` to `"dark"`

## Your tasks

1. `cd` into the sandbox and look around:

   ```bash
   git log --oneline --graph --all
   ```

2. Merge the feature branch into `main`:

   ```bash
   git merge feature/dark-mode
   ```

   Git reports `CONFLICT (content): Merge conflict in settings.py`.

3. Run `git status`. Which file is listed under "Unmerged paths"?

4. Open `settings.py`. You'll see:

   ```text
   <<<<<<< HEAD
   THEME = "uwec-blue"
   =======
   THEME = "dark"
   >>>>>>> feature/dark-mode
   ```

   The top half is your current branch (`main`); the bottom half is the incoming one.
   Notice that the `MAX_USERS` change merged on its own, because nobody else touched that line.

5. Decide what the line should be. Keep one side, or write something new such as
   `THEME = "dark"` plus a new line `ACCENT = "uwec-blue"`. Delete all three
   marker lines (`<<<<<<<`, `=======`, `>>>>>>>`).

6. Finish the merge:

   ```bash
   git add settings.py
   git commit
   ```

   Git opens an editor with a merge message already written. Save and close it.
   (Stuck in Vim? Type `:wq` and press Enter.)

7. Check your work: `git log --oneline --graph`. You should see the two lines of history join.

## Stretch goals

- Run the setup again, and this time back out with `git merge --abort`.
- In VS Code, open the conflicted file and try the **Accept Current / Accept
  Incoming / Accept Both** buttons.

<details>
<summary>How do I know I'm done?</summary>

`git status` says "nothing to commit, working tree clean", `settings.py`
contains no `<<<<<<<`, `=======`, or `>>>>>>>` lines, and `git log` shows a
commit starting with "Merge branch 'feature/dark-mode'".
</details>

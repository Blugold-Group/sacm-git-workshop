# Exercise: Undo things

Everyone makes mistakes in Git. The skill is knowing which undo to reach for.

## Set up

From the root of the workshop repo:

```bash
bash exercises/03-undo/setup.sh
cd playground/undo
```

Run `git status` and `git log --oneline` to see what you're working with.
Then fix these four mistakes, **in this order**.

## 1. Unstage the secrets file

`.env` is staged, and it should never be committed.

- Unstage it without deleting it.
- Stop Git from suggesting it again.

<details>
<summary>Hint</summary>

`git restore --staged <file>`, then create a `.gitignore` file.
</details>

<details>
<summary>Solution</summary>

```bash
git restore --staged .env
echo ".env" > .gitignore
git status        # .env is gone from the list; .gitignore is new
```

Don't commit `.gitignore` yet. You'll do that at the end.
</details>

## 2. Throw away the debugging line

`grades.py` has an uncommitted `print('debugging!!!')` at the end.
Discard that change.

<details>
<summary>Hint</summary>

`git restore <file>` puts a file back to how it was in the last commit.
**It can't be undone**, so check `git diff` first.
</details>

<details>
<summary>Solution</summary>

```bash
git diff grades.py
git restore grades.py
```
</details>

## 3. Fix the typo in a commit message

"Updaet readme" should be "Update readme".

<details>
<summary>Hint</summary>

`git commit --amend` rewrites the **most recent** commit. Only amend
commits you haven't pushed yet.
</details>

<details>
<summary>Solution</summary>

```bash
git commit --amend -m "Update readme"
git log --oneline
```
</details>

## 4. Undo the broken "Optimize average" commit

Dividing by zero is not an optimization. Undo that commit **without
rewriting history**, as you would on a branch other people use.

<details>
<summary>Hint</summary>

`git revert <commit>` makes a new commit that does the opposite. Find the
commit's ID with `git log --oneline`.
</details>

<details>
<summary>Solution</summary>

```bash
git log --oneline            # find the ID next to "Optimize average"
git revert <that-id>         # save and close the editor
cat grades.py                # dividing by len(scores) again
```
</details>

## Wrap up

Commit the `.gitignore` from mistake 1:

```bash
git add .gitignore
git commit -m "Ignore .env"
git status        # clean, and .env is still not listed
```

## Bonus: The safety net

Run `git reflog`. It lists every place `HEAD` has been, including commits
you "lost" with `reset` or `amend`. Try it:

```bash
git reset --hard HEAD~2      # oh no!
git reflog                   # find the commit you were on before the reset
git reset --hard <that-id>   # back again
```

As long as you committed it, Git almost never truly loses it.

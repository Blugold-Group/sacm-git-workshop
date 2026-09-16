# Exercise: Branching

Build a small project with two feature branches and merge them both.

## Set up

From the root of the workshop repo:

```bash
bash exercises/04-branching/setup.sh
cd playground/branching
```

This sandbox has one commit on `main`: a `menu.txt` for a club pizza night.

## Your tasks

1. **Drinks.** Create a branch named `feature/drinks`. Create `drinks.txt`
   listing a few drinks and commit it.

2. **Toppings.** Switch back to `main`. Is `drinks.txt` there? (It
   shouldn't be. It only exists on the other branch.) Create
   `feature/toppings` from `main`, add a few lines to the end of
   `menu.txt`, and commit. Make at least **two** commits on this branch.

3. **Look at the graph.**

   ```bash
   git log --oneline --graph --all
   ```

   You should see two branches forking off the same commit.

4. **Merge.** Switch to `main` and merge both branches:

   ```bash
   git switch main
   git merge feature/drinks
   git merge feature/toppings
   ```

   The first merge is a *fast-forward*. The second creates a *merge commit*.
   Look at the graph again. Can you explain why they're different?

5. **Clean up.** Delete both branches with `git branch -d <name>`.

<details>
<summary>Why was the first merge a fast-forward?</summary>

When you merged `feature/drinks`, `main` hadn't moved since that branch was
created. Git just slid the `main` label forward. After that, `main` and
`feature/toppings` had both moved on from their common starting point, so
Git needed a merge commit to join them.
</details>

## Keep going

[Learn Git Branching](https://learngitbranching.js.org) teaches branches,
merging, and rebasing visually. Do the "Introduction Sequence" levels next.

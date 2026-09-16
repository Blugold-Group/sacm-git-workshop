# SACM Git & GitHub Workshop

Welcome! This repo is a safe place to practice Git and GitHub. You can't break
anything here, so experiment freely.

**Your goal today:** open your first pull request by adding a file about yourself
to the [`members/`](members/) folder.

> **Before you start:** install Git ([git-scm.com](https://git-scm.com)), make a
> [GitHub account](https://github.com/signup), and tell Git who you are:
>
> ```bash
> git config --global user.name "Your Name"
> git config --global user.email "you@uwec.edu"
> ```

---

## Part 1: Your first pull request (about 15 minutes)

### 1. Fork this repo

Click **Fork** in the top-right corner of this page. This makes your own copy
under your GitHub account, and you're allowed to push to that copy.

### 2. Clone your fork

On **your fork's** page, click the green **Code** button and copy the URL. Then:

```bash
git clone https://github.com/YOUR-USERNAME/sacm-git-workshop.git
cd sacm-git-workshop
```

> **Sign-in help:** GitHub doesn't accept your account password in the terminal.
> The easiest option is the [GitHub CLI](https://cli.github.com): run
> `gh auth login` once. SSH keys or a personal access token also work.

### 3. Create a branch

```bash
git switch -c add-YOUR-USERNAME
```

### 4. Add your member file

Copy the template, naming the new file after your GitHub username (it's
case-sensitive and must match exactly):

```bash
cp members/_template.md members/YOUR-USERNAME.md
```

Open `members/YOUR-USERNAME.md` in any editor and fill it in.

### 5. Commit

```bash
git status                     # your new file shows up in red
git add members/YOUR-USERNAME.md
git status                     # now it's green (staged)
git commit -m "Add YOUR-USERNAME to members"
```

### 6. Push

```bash
git push -u origin add-YOUR-USERNAME
```

### 7. Open the pull request

Go to your fork on GitHub. You should see a yellow banner with a
**Compare & pull request** button. Click it, fill in the template, and submit.

### 8. Watch the checks

An automated check runs on your pull request to make sure your file is filled
in correctly. If it fails, click **Details** to see what to fix. Then fix the
file, commit, and push again: the pull request updates automatically.

When the check is green, an officer will review and merge it. 🎉

---

## Part 2: Bonus exercises

Finished early? Work through these on your own machine:

| Exercise | What you'll practice |
| --- | --- |
| [Merge conflicts](exercises/02-merge-conflict/) | Making a conflict on purpose and resolving it |
| [Undoing things](exercises/03-undo/) | `restore`, `amend`, `revert`, and `reflog` |
| [Branching](exercises/04-branching/) | Building a branch history and merging it |

The exercises use small shell scripts. On Windows, run them in **Git Bash**,
which comes with Git for Windows.

## Cheat sheet

| I want to… | Command |
| --- | --- |
| See what changed | `git status`, `git diff` |
| Stage a file | `git add <file>` |
| Commit staged changes | `git commit -m "Message"` |
| See history | `git log --oneline --graph` |
| Create and switch to a branch | `git switch -c <name>` |
| Switch branches | `git switch <name>` |
| Get the latest from GitHub | `git pull` |
| Send your commits to GitHub | `git push` |
| Discard edits to a file | `git restore <file>` |
| Unstage a file | `git restore --staged <file>` |

## Keep learning

- [Pro Git](https://git-scm.com/book), the free book
- [Learn Git Branching](https://learngitbranching.js.org), an interactive visual tutorial
- [GitHub Skills](https://skills.github.com), guided courses that run in real repos
- [Dangit, Git!?](https://dangitgit.com), plain-English fixes for common mistakes

---

Made for SACM, the student ACM chapter at UW–Eau Claire. Officers, see
[docs/officer-guide.md](docs/officer-guide.md) before the workshop.

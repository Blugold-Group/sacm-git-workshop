# 🗿 SACM Git & GitHub Workshop: SIGMA VERITY EDITION

 Welcome to the **Git arena**.

 This repo is a safe place to practice Git and GitHub. You cannot break anything here.

 **Unless you skill issue.**

 Your objective is simple:

 > **OPEN THE PULL REQUEST.**
>
>  Add a file about yourself to `members/`.
>
>  Become one with the branch.
>
>  Embrace **VERITY**.

---

 ## ⚡ BEFORE YOU LOCK IN

 Install Git:

 - [Git](<https://git-scm.com>)
- [GitHub](<https://github.com/signup>)

 Then establish your identity:

```
git config --global user.name "Your Name"
git config --global user.email "you@uwec.edu"
```

 If Git asks who you are, **DO NOT PANIC.**

 Git simply needs to know the identity of the warrior performing the commit.

---

 # 🗿 PART 1: YOUR FIRST PULL REQUEST

 **Estimated time: 15 minutes**

 **Difficulty: literally just follow the instructions**

 **Aura requirement: nonzero**

 ## 1\. FORK THE REPO

 Click **Fork** in the top-right.

 This creates your own copy.

 Your repo.

 Your branch.

 Your destiny.

 You may now push to it.

 **VERITY ACHIEVED.**

---

 ## 2\. CLONE YOUR FORK

 On **your fork**, click the green **Code** button and copy the URL.

 Then:

```
git clone https://github.com/YOUR-USERNAME/sacm-git-workshop.git
cd sacm-git-workshop
```

 Congratulations.

 You have acquired the repository.

 ### 🧠 SIGN-IN LORE

 GitHub does not accept your account password in the terminal.

 The sigma path is the [GitHub CLI](<https://cli.github.com>):

```
gh auth login
```

 SSH keys and personal access tokens also work.

 **Authentication is not optional.**

---

 ## 3\. CREATE YOUR BRANCH

```
git switch -c add-YOUR-USERNAME
```

 You have now escaped `main`.

 You are no longer merely a contributor.

 You are **BRANCHED.**

 > A branch is simply a timeline where your changes happen.
>
>  **Do not merge the wrong timeline.**

---

 ## 4\. ADD YOUR MEMBER FILE

 Copy the template:

```
cp members/_template.md members/YOUR-USERNAME.md
```

 Replace `YOUR-USERNAME` with your **actual GitHub username**.

 It is case-sensitive.

 Open the file.

 Fill it out.

 Do not submit `_template.md`.

 That would be an **unfortunate display of low verity**.

---

 ## 5\. COMMIT YOUR EXISTENCE

 Check your status:

```
git status
```

 Your new file should appear in red.

 Then:

```
git add members/YOUR-USERNAME.md
```

 Check again:

```
git status
```

 Green.

 **GREEN = STAGED.**

 Then commit:

```
git commit -m "Add YOUR-USERNAME to members"
```

 You have created history.

 History cannot be unmade.

 Well, technically it can.

 But that comes later.

---

 ## 6\. PUSH

 Send your branch into the cloud:

```
git push -u origin add-YOUR-USERNAME
```

 Your code has left the machine.

 It is now **out there.**

 There is no going back.

 > `git push`
>
>  **The button has been pressed.**

---

 ## 7\. OPEN THE PULL REQUEST

 Go to your fork on GitHub.

 You should see a yellow banner.

 It will contain:

 **Compare & pull request**

 Click it.

 Fill out the template.

 Submit.

 At this point, you have entered the sacred realm of:

 # 🔥 PULL REQUEST

---

 ## 8\. WATCH THE CHECKS

 An automated check will inspect your file.

 If it fails:

 **DO NOT CRUMBLE.**

 Click **Details**.

 Read the error.

 Fix the file.

 Commit.

 Push.

 The pull request updates automatically.

 This is the Git cycle:

```
EDIT
  ↓
COMMIT
  ↓
PUSH
  ↓
CHECK
  ↓
FAIL
  ↓
FIX
  ↓
COMMIT
  ↓
PUSH
  ↓
VERITY
```

 When the check is green, an officer will review and merge it.

 🎉 **YOU HAVE CONTRIBUTED.**

 Your GitHub graph has received another pixel.

 Your aura has increased by approximately 0.00001.

---

 # 🗿 PART 2: BONUS SIGMA EXERCISES

 Finished early?

 **You have chosen violence.**

 Work through these on your own machine:

 | Exercise | What you will learn |
| --- | --- |
| Merge conflicts | Create conflict. Become conflict. Resolve conflict. |
| Undoing things | `restore`, `amend`, `revert`, and `reflog` — forbidden techniques |
| Branching | Create timelines. Merge timelines. Become timeline manager. |

The exercises use small shell scripts.

 On Windows, use **Git Bash**, which comes with Git for Windows.

 PowerShell may be watching.

---

 # ⚔️ CHEAT SHEET OF VERITY

 | I want to… | Command | Sigma Translation |
| --- | --- | --- |
| See what changed | `git status`, `git diff` | **Observe.** |
| Stage a file | `git add <file>` | **Prepare the offering.** |
| Commit changes | `git commit -m "Message"` | **Create history.** |
| See history | `git log --oneline --graph` | **Study the ancient texts.** |
| Create a branch | `git switch -c <name>` | **Escape the timeline.** |
| Switch branches | `git switch <name>` | **Change universes.** |
| Get the latest | `git pull` | **Acquire knowledge.** |
| Send commits | `git push` | **Release the beast.** |
| Discard edits | `git restore <file>` | **It never happened.** |
| Unstage a file | `git restore --staged <file>` | **Return the offering.** |

---

 # 🧠 KEEP LEARNING

 The path to greater Git verity:

 - [Pro Git](<https://git-scm.com/book>) — the free book
- [Learn Git Branching](<https://learngitbranching.js.org>) — interactive visual Git combat
- [GitHub Skills](<https://skills.github.com>) — guided courses inside real repositories
- [Dangit, Git!?](<https://dangitgit.com>) — when Git has decided that you are no longer worthy

---

 # 🗿 FINAL VERITY

 You started with:

```
"I don't know Git."
```

 You leave with:

```
"I have forked."
"I have branched."
"I have committed."
"I have pushed."
"I have opened the PR."
```

 You are now dangerous.

 Use your powers responsibly.

---

 Made for **SACM**, the student ACM chapter at UW–Eau Claire.

 Officers:

 Read `docs/officer-guide.md` before the workshop.

 **Stay sigma.**

 **Commit often.**

 **Push responsibly.**

 **Seek verity.**

 # 🗿

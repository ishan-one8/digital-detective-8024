# Mission 6 - Git and GitHub

## 1. Task / objective
Understand version control: check status, stage and commit changes, view history, create a branch, open a Pull Request on GitHub, and explain why this workflow helps people collaborate.

## 2. Work completed
- Practised the basic workflow — `status` → `add` (one specific README) → `commit` → `log` (Task 6.1).
- Created the branch **`update-about`**, added a **"My Learning"** section to the root `README.md`, committed it and published the branch to GitHub (Task 6.2).
- Opened **Pull Request #1** from `update-about` into `main`, reviewed the changed file, **merged it**, then switched back to `main` locally and pulled the merged changes (Task 6.3).
- Wrote a Git command glossary (Task 6.4).

### Task 6.1 - Basic Git workflow
For this step I checked the status, staged **only** this mission's README file, committed it and looked at the history.
Output: [`evidence/mission-06-task6.1-output.txt`](../evidence/mission-06-task6.1-output.txt)

| Git operation | Command | What it does in my own words |
|---------------|---------|------------------------------|
| Check repository status | `git status` | Tells me which branch I am on and which files are new, changed, or already staged — a "what's going on" check before doing anything. |
| Stage selected changes | `git add mission-06-git-github/README.md` | Puts the chosen file into the **staging area** — a waiting room of changes that will go into the next commit. Other changed files are not included. |
| Create a commit | `git commit -m "message"` | Takes everything in the staging area and saves it permanently in the history as one snapshot, with my message, name and time. |
| View commit history | `git log --oneline` | Lists previous commits (newest first) with their short ID and message, so I can see how the project developed. |

**Staging vs committing:** staging (`git add`) is like *choosing which photos to put in an envelope*; committing (`git commit`) is *sealing the envelope and labelling it*. Staging lets me pick exactly which changes belong together, so one commit = one meaningful piece of work. A staged change can still be removed or changed; a commit is a saved point in history that I can always come back to.

### Task 6.2 - Create and use a branch
Commands used (full output in [`evidence/mission-06-branch-pr-output.txt`](../evidence/mission-06-branch-pr-output.txt)):
```bash
git switch -c update-about                 # create the branch and move onto it
# edited README.md -> added "## My Learning" with 3 points
git status                                 # README.md shown as modified
git add README.md
git commit -m "Add My Learning section to README"
git push -u origin update-about            # publish the new branch to GitHub
```

### Task 6.3 - Pull Request
1. Opened the repository on GitHub and compared `update-about` with `main`.
2. Created **Pull Request #1: "Add My Learning section to README"** from `update-about` → `main`, with a short description of the change.
3. Reviewed the **Files changed** tab: only `README.md`, **8 lines added**, nothing removed.
4. **Merged** the PR (merge commit `Merge pull request #1 from update-about`).
5. Back in Terminal: `git switch main` then `git pull` — Git fast-forwarded my local `main` to include the merged README.

**PR status: ✅ MERGED** — https://github.com/ishan-one8/digital-detective-8024/pull/1

`git log --oneline --graph` after the merge shows the branch joining back into `main`:
```
*   1e4e892 Merge pull request #1 from update-about
|\
| * 82dfcf9 Add My Learning section to README
|/
* e6b0507 Build number converter and practise data representation
```

**What is a branch?** A branch is a separate line of work inside the same repository. I can make changes on `update-about` without touching `main`, so the main version always stays working.

**What is a Pull Request?** A Pull Request is a request on GitHub that says *"please pull the changes from my branch into main"*. It shows exactly which lines changed, and others can review, comment and approve before it is merged.

**Why they are useful when people work together:** several people can each work on their own branch at the same time without overwriting each other's work. The Pull Request is the checkpoint where teammates review the code, catch mistakes, and discuss before anything enters the main project — and the history keeps a record of who changed what and why.

### Task 6.4 - Git command glossary

| Operation | Command | One-line explanation |
|-----------|---------|----------------------|
| Initialise a repository | `git init` | Turns a normal folder into a Git repository by creating the hidden `.git` folder that stores the history. |
| Check status | `git status` | Shows the current branch and which files are changed, staged or untracked. |
| Stage changes | `git add <file>` | Selects changes to include in the next commit. |
| Commit changes | `git commit -m "msg"` | Saves the staged changes as a permanent snapshot with a message. |
| View history | `git log --oneline` | Lists past commits with their IDs and messages. |
| Create or list branches | `git branch` / `git branch <name>` | With no name it lists branches (`*` marks the current one); with a name it creates a new branch. |
| Switch branches | `git switch <name>` (`-c` to create and switch) | Moves my working folder to another branch's version of the files. |
| Publish changes | `git push` (`-u origin <branch>` the first time) | Uploads my local commits to GitHub. |
| Retrieve remote changes | `git pull` | Downloads new commits from GitHub and merges them into my current branch. |

## 3. Commands / tools used
| Command / tool | Purpose |
|----------------|---------|
| `git status` | Check what has changed and what is staged. |
| `git add` | Stage a specific file. |
| `git commit -m` | Save a snapshot with a meaningful message. |
| `git log --oneline --graph` | View history and see the branch/merge shape. |
| `git switch -c update-about`, `git switch main` | Create a branch / move between branches. |
| `git branch` | List local branches. |
| `git push -u origin update-about` | Publish the new branch. |
| `git pull` | Bring the merged changes into local `main`. |
| GitHub website (Compare & pull request, Files changed, Merge) | Open, review and merge the Pull Request. |
| GitHub CLI `gh pr create`, `gh pr merge` | Same PR actions from the Terminal. |

## 4. My understanding
Git is like an unlimited "undo history" for a whole project, where I decide when to save (commit) and what goes into each save (staging). Because every mission in this assignment has its own commit, anyone can open the history and see the project grow step by step. Branches let me experiment safely, and Pull Requests turn merging into a reviewable step instead of directly changing `main`. The graph after merging made it very clear: the branch went off to the side, got one commit, and then joined back.

## 5. Difficulties faced
1. I edited `README.md` before creating the branch and worried the change would go onto `main`.
2. After merging on GitHub, my local `main` did not show the "My Learning" section.

## 6. How I resolved them
1. I learned that uncommitted changes move with me when I run `git switch -c`, so the edit ended up on `update-about`. `git status` confirmed I was on the new branch before I committed.
2. Merging on GitHub only changes the online copy. I ran `git switch main` and `git pull` to download the merge commit, and then the section appeared locally.

## 7. Evidence / files
- `evidence/mission-06-task6.1-output.txt` — status, add, commit and log for Task 6.1.
- `evidence/mission-06-branch-pr-output.txt` — branch creation, push, and switch/pull after merge.
- Pull Request #1 on GitHub (merged).
- Root `README.md` — now contains the "My Learning" section.

## 8. Commit details
- Branch commit: **`Add My Learning section to README`** (on `update-about`, merged via PR #1).
- Mission commit: **`Complete Git and GitHub collaboration mission`** — pushed to GitHub on `main` and verified online.

# Mission 8 - Final report and submission

## 1. Task / objective
Review the whole repository, make the root README useful to a first-time visitor, confirm every mission has its own README and commit, remove any private information, and submit the repository URL.

## 2. Work completed
- Checked the repository structure against the required layout — every folder and file is present.
- Confirmed all 9 mission READMEs use the same 8 headings with no blank sections.
- Updated the root `README.md` with an introduction, mission index, topics explored, instructions to run the converter, a learning summary and a note on separate commits.
- Re-ran `number_converter.py` to confirm it still works.
- Scanned every file for personal details before the final push.

### Step 1 - Repository structure check

| Required path | Present? | Contents |
|---------------|----------|----------|
| `README.md` | ✅ | Overview, mission links, topics, converter instructions, learning summary. |
| `mission-00-setup/README.md` | ✅ | Setup, tool versions, structure. |
| `mission-01-computer-basics/README.md` | ✅ | IPOS, hardware/software, everyday systems. |
| `mission-02-terminal/README.md` | ✅ | Terminal practice, flags, pipes, Homebrew (+ `practice/`, `terminal-practice/`). |
| `mission-03-operating-system/README.md` | ✅ | OS info, processes, paths, permissions, OS responsibilities. |
| `mission-04-programs/README.md` + `hello.py` | ✅ | Program execution and compiler vs interpreter. |
| `mission-05-numbers-data/README.md` + `number_converter.py` | ✅ | Conversions, Python verification, encoding, working converter. |
| `mission-06-git-github/README.md` | ✅ | Git workflow, branch, Pull Request, glossary. |
| `mission-07-networking/README.md` | ✅ | Network concepts, ping/DNS observations, website steps. |
| `mission-08-final-report/README.md` | ✅ | This file. |
| `evidence/` | ✅ | 11 privacy-safe Terminal output files. |

### Mission status

| Mission | Status | Commit message |
|---------|--------|----------------|
| 0 - Setup | ✅ Complete | Set up Digital Detective mission structure |
| 1 - Computer basics | ✅ Complete | Complete computer basics and IPOS mission |
| 2 - Terminal | ✅ Complete | Complete Terminal and file management mission |
| 3 - Operating system | ✅ Complete | Document operating system and file management |
| 4 - Programs | ✅ Complete | Compare compilers and interpreters |
| 5 - Numbers and data | ✅ Complete | Build number converter and practise data representation |
| 6 - Git and GitHub | ✅ Complete — PR #1 **merged** | Add My Learning section to README (branch) · Complete Git and GitHub collaboration mission |
| 7 - Networking | ✅ Complete | Explain networking concepts and website communication |
| 8 - Final report | ✅ Complete | Complete final report and verify assignment submission |

### Corrections made during the final review
- Replaced my username, device name, disk ID and router address with `[redacted]` in every evidence file.
- Made sure the commit ID in the Mission 6 evidence matches the real merge commit shown in the history.
- Added `.gitignore` entries for `.DS_Store` and `__pycache__/` so system and generated files are not committed.
- Expanded the root README so a visitor can understand the project and run the converter without opening other files.

### Step 4 - Final checklist
- [x] All mission folders are present and each has its own README.md.
- [x] Every mission README records the task, commands/tools used, understanding and difficulties.
- [x] Every mission has its own meaningful commit, and all required commits are pushed.
- [x] IPOS, hardware, software and computer-system examples are included.
- [x] Terminal operations, file management, flags and pipes are explained.
- [x] Operating system, processes, paths, storage and permissions are covered.
- [x] Compiler and interpreter are compared.
- [x] Number conversions include working and Python verification.
- [x] The number_converter.py program runs successfully with at least three test values (13, 25, 255, 2026).
- [x] Git commit history, branch and Pull Request activity are visible.
- [x] LAN, MAN, WAN, DNS, router, protocols and client-server are explained.
- [x] The root README explains the project and how to run the converter.
- [x] Personal information has been removed from screenshots and outputs.
- [x] All final changes are committed and pushed to GitHub.

### Step 5 - Submission
- Repository: **https://github.com/ishan-one8/digital-detective-8024** (public)
- Confirmed the repository is public and the latest commit is visible on GitHub.
- The URL is submitted through the Google Form shared by the instructor.

## 3. Commands / tools used
| Command / tool | Purpose |
|----------------|---------|
| `find`, `ls` | Check that every required folder and file exists. |
| `grep -c '^## '` | Count the headings in each mission README to make sure none is missing. |
| `grep -rn` | Search all files for my username, device name or private IP addresses before pushing. |
| `python3 number_converter.py` | Re-test the converter one last time (input 7 → binary 111, hex 7). |
| `git status`, `git log --oneline` | Confirm there are no uncommitted changes and every mission has its own commit. |
| `git add`, `git commit`, `git push` | Save and publish the final report. |
| GitHub website | Verify files, commits, the branch and the merged Pull Request online. |

## 4. My understanding
The final review showed me why documenting as I go matters: because every mission had its own README and commit, checking the whole project took minutes, and anyone (including my instructor) can see exactly what I did and in what order. A good root README is the "front door" of a repository — it should tell a stranger what the project is and how to use it. I also learned that privacy is something to check at the end on purpose, not assume, because Terminal output can easily include usernames, device names and IP addresses.

## 5. Difficulties faced
While reviewing, I noticed that one commit ID written in my Mission 6 evidence did not match the ID shown in the final history.

## 6. How I resolved them
I compared the evidence with `git log --oneline --graph`, updated the evidence to show the correct merge commit ID, and checked again with `grep` that no old ID remained.

## 7. Evidence / files
- `README.md` (root) — final project overview.
- `mission-08-final-report/README.md` — this review and checklist.
- All files listed in the structure table above.

## 8. Commit details
- Commit message: **`Complete final report and verify assignment submission`**
- Pushed to GitHub on `main`; files and commit verified on GitHub.

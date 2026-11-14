# Mission 0 - Create your GitHub workspace

## 1. Task / objective
Create a correctly named public GitHub repository and prepare a clean folder structure so that every mission has its own place.

## 2. Work completed
- Decided the repository name using the rule *assignment name + last four USN digits*: **`digital-detective-8024`**.
- Created a local project folder with exactly the same name and opened it in Terminal and in my editor.
- Checked that Python 3 and Git are installed.
- Created one folder per mission (`mission-00-setup` … `mission-08-final-report`), an empty `README.md` inside each, the empty `number_converter.py` file for Mission 5, and an `evidence/` folder.
- Wrote the root `README.md` with a title, description and mission index.
- Turned the folder into a Git repository, made the first commit and published it as a **public** GitHub repository with the same name.

### Tools checked

| Tool | Command used | Version found |
|------|--------------|---------------|
| Python 3 | `python3 --version` | Python 3.14.5 |
| Git | `git --version` | git version 2.55.0 |
| GitHub CLI (extra) | `gh --version` | used to create the online repository |
| Operating system | `sw_vers` | macOS 27.2.1 |

### Folders and files created
```
digital-detective-8024/
├── README.md
├── evidence/
├── mission-00-setup/README.md
├── mission-01-computer-basics/README.md
├── mission-02-terminal/README.md
├── mission-03-operating-system/README.md
├── mission-04-programs/README.md
├── mission-05-numbers-data/README.md
├── mission-05-numbers-data/number_converter.py
├── mission-06-git-github/README.md
├── mission-07-networking/README.md
└── mission-08-final-report/README.md
```

## 3. Commands / tools used
| Command / tool | Purpose |
|----------------|---------|
| `python3 --version`, `git --version` | Confirm both tools are installed before starting. |
| `mkdir` | Make the project folder and the mission folders. |
| `touch` | Create the empty `README.md` files and `number_converter.py`. |
| `cd` | Move into the project folder. |
| `git init -b main` | Turn the folder into a Git repository whose main branch is called `main`. |
| `git add`, `git commit` | Stage the setup files and save them as the first snapshot. |
| `gh repo create --public --source . --push` | Create the public repository on GitHub, connect it as `origin` and push. |
| VS Code | Editing the Markdown files. |

## 4. My understanding
A **repository** is a project folder that Git is watching. Git keeps a full history of every saved change (commit), so I can see what changed, when, and go back if I break something. GitHub stores a copy of the repository online so others (my instructor) can see it.

The structure is **organised by mission** because each mission is a separate topic. Keeping each in its own folder with its own README makes the repo easy to navigate, keeps files from getting mixed up, and lets each mission have its own clean commit in the history. The folder name and repository name must match so that the local copy and the online copy are clearly the same project.

## 5. Difficulties faced
While creating the empty README files I first used a shell wildcard (`mission-0*-*/README.md`) and got `no matches found`, because the README files did not exist yet so the pattern could not match anything.

## 6. How I resolved them
I understood that a wildcard only matches files that already exist. I used a simple loop instead: `for d in mission-0*; do touch $d/README.md; done`, which goes through each existing folder and creates the file inside it.

## 7. Evidence / files
- `README.md` (root) — project introduction and mission index.
- `mission-00-setup/README.md` — this file.
- The empty folder structure shown above.

## 8. Commit details
- Commit message: **`Set up Digital Detective mission structure`**
- Pushed to GitHub on branch `main` and verified that all folders are visible online.

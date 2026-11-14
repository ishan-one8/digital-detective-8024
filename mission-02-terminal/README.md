# Mission 2 - Become comfortable with the Terminal

## 1. Task / objective
Use the command-line interface (CLI) to inspect folders, create and manage practice files safely, understand how flags and pipes change a command, and explain what a package manager does.

## 2. Work completed
- Practised 9 basic Terminal operations inside this mission folder and recorded what each does (Task 2.1).
- Created the `terminal-practice/` folder, wrote two lines into a file using `>` and `>>`, made a backup and renamed it (Task 2.2).
- Compared `ls`, `ls -l`, `ls -la` and `ls -lah`, and used a pipe `|` with `head` (Task 2.3).
- Checked Homebrew's version and the list of packages it manages, **without installing or removing anything** (Task 2.4).
- All work stayed inside this repository. No administrator (`sudo`) commands were used.

### Task 2.1 - Basic Terminal operations

| Operation | Command | What it does | What I observed |
|-----------|---------|--------------|-----------------|
| Current-directory display | `pwd` | Prints the full path of the folder I am working in ("print working directory"). | It showed a long path ending in `.../digital-detective-8024/mission-02-terminal` (my username is redacted). |
| Directory listing | `ls` | Lists the names of files and folders in the current location. | Only `README.md` was there at the start. |
| Detailed listing | `ls -l` | Lists items in "long" format: permissions, owner, size, date and name. | `-rw-r--r-- ... 0 Nov 15 03:37 README.md` — size 0 because the README was still empty. |
| Change directory | `cd ..` | Moves to the parent folder (`..` means "one level up"). | `pwd` changed from `.../mission-02-terminal` to `.../digital-detective-8024`. |
| Create directory | `mkdir practice` | Makes a new folder. | `ls` now showed `practice` next to `README.md`. |
| Create empty file | `touch practice/sample.txt` | Creates an empty file (or updates the time of an existing one). | `ls practice` showed `sample.txt`. |
| Copy file | `cp practice/sample.txt practice/sample-copy.txt` | Makes a duplicate; the original stays. | Both `sample.txt` and `sample-copy.txt` appeared. |
| Move / rename file | `mv practice/sample-copy.txt practice/renamed-copy.txt` | Moves a file to a new name or place; the old name disappears. | `sample-copy.txt` was gone and `renamed-copy.txt` appeared. |
| Display file contents | `cat practice/sample.txt` | Prints the contents of a file in the Terminal. | Nothing was printed, because the file was empty — this was what I predicted. |

Full output: [`evidence/mission-02-task2.1-output.txt`](../evidence/mission-02-task2.1-output.txt)

### Task 2.2 - Practise file changes safely
Commands used inside `mission-02-terminal/terminal-practice/`:
```bash
echo "Line 1: I am learning the Terminal." > notes.txt
echo "Line 2: >> adds text without deleting line 1." >> notes.txt
cat notes.txt
cp notes.txt notes-backup.txt
mv notes-backup.txt notes-backup-diwali.txt
```
`cat notes.txt` showed **both lines**, and the renamed backup `notes-backup-diwali.txt` has the same two lines.
Full output: [`evidence/mission-02-task2.2-output.txt`](../evidence/mission-02-task2.2-output.txt)

**Answers:**
- **Replacing vs adding to the end:** `>` *replaces* — it empties the file first and then writes, so old content is lost. `>>` *appends* — it adds the new text to the end and keeps what was already there. That is why my second line used `>>`.
- **Copying vs moving:** `cp` creates a second file and the original stays where it was (two files). `mv` does not create anything new — it changes the file's name or location, so there is still only one file.
- **What the current-directory display (`pwd`) tells me:** exactly where I am in the folder tree, as a full (absolute) path from the root `/`. This matters because commands like `touch` or `rm` act on the current folder.
- **Why a directory listing (`ls`) is useful:** it lets me check what is in a folder before and after a command, so I can confirm a file was really created, copied or renamed, and avoid typos in file names.

### Task 2.3 - Flags and pipes
Full output: [`evidence/mission-02-task2.3-output.txt`](../evidence/mission-02-task2.3-output.txt)

| Command | What changed |
|---------|--------------|
| `ls` | Just names: `README.md  practice  terminal-practice`. |
| `ls -l` | Each item on its own line with permissions (`drwxr-xr-x`), number of links, owner, group, size in bytes, date and name. A `d` at the start means directory. |
| `ls -la` | Same as `-l` but **also shows hidden items** whose names start with a dot, e.g. `.` (this folder) and `..` (parent folder). In the repo root it also shows `.git` and `.gitignore`. |
| `ls -lah` | Same as `-la` but sizes are **human-readable**: `128B` instead of `128`; large files show `K`, `M`, `G`. |

So a **flag** (like `-l`, `-a`, `-h`) does not change *which* command runs, it changes *how* it behaves. Flags can be combined: `-lah` = `-l` + `-a` + `-h`.

**Pipe:** `ls -lah .. | head -5`
- Left side `ls -lah ..` produces a detailed listing of the parent folder.
- The pipe `|` takes that output and, instead of printing it, **feeds it as input** to the next command.
- Right side `head -5` keeps only the first 5 lines and prints them.

Result: I only saw the first 5 lines (`total`, `.`, `..`, `.git`, `.gitignore`). A pipe lets me join small commands together into a bigger tool.

### Task 2.4 - Package managers
Homebrew is installed on my Mac. I only ran read-only commands:
- `brew --version` → `Homebrew 7.0.9`
- `brew list --formula | wc -l` → **87** packages managed (another pipe: `wc -l` counts lines)
- `brew list --formula | head -10` → first ten, e.g. `autoconf`, `cmake`, `cowsay`

Full output: [`evidence/mission-02-task2.4-output.txt`](../evidence/mission-02-task2.4-output.txt)

**Why package managers are useful:** a package manager installs, updates and removes software with one command, instead of me searching websites and downloading installers by hand. It also automatically installs the other packages a tool depends on, and keeps a list of what is installed so updating everything (`brew upgrade`) or removing something cleanly is easy. This is safer and faster, especially for developer tools.

## 3. Commands / tools used
| Command | Purpose |
|---------|---------|
| `pwd` | Show the current folder's full path. |
| `ls`, `ls -l`, `ls -la`, `ls -lah` | List folder contents in different levels of detail. |
| `cd`, `cd ..` | Change folder / go up one level. |
| `mkdir` | Create a folder. |
| `touch` | Create an empty file. |
| `cp` | Copy a file. |
| `mv` | Move or rename a file. |
| `cat` | Print file contents. |
| `echo "..." >` / `>>` | Write (replace) / append a line of text into a file. |
| `head -5` | Show only the first 5 lines of input. |
| `wc -l` | Count lines. |
| `|` (pipe) | Send the output of one command into another. |
| `brew --version`, `brew list` | Check Homebrew and list its packages (read-only). |

## 4. My understanding
The Terminal is a text way of doing what Finder does with clicks, but it is faster and more precise once you know the commands, and the commands can be combined. Every command acts on the **current directory** unless I give a path, so `pwd` and `ls` are my "where am I / what's here" checks before doing anything. The biggest lesson was the difference between `>` and `>>`: one wrong character can wipe a file, which is why the assignment asked me to practise only inside a practice folder. Flags customise a command, and pipes connect commands into a chain.

## 5. Difficulties faced
1. `ls -la` inside this mission folder looked almost the same as `ls -l` — I expected to see hidden files but only `.` and `..` appeared.
2. When I saved output into the `evidence/` folder with a relative path (`../evidence/...`) after changing folders, I got `no such file or directory`.

## 6. How I resolved them
1. I realised this folder simply had no hidden files. Running `ls -la` from the repository root showed `.git` and `.gitignore`, which proved `-a` works.
2. The relative path was wrong because I was one folder deeper than I thought. I checked with `pwd` and then used the correct path. Lesson: relative paths always depend on where you currently are.

## 7. Evidence / files
- `practice/sample.txt`, `practice/renamed-copy.txt` — Task 2.1 files.
- `terminal-practice/notes.txt`, `terminal-practice/notes-backup-diwali.txt` — Task 2.2 files.
- `evidence/mission-02-task2.1-output.txt` … `mission-02-task2.4-output.txt` — privacy-safe Terminal output (username replaced with `[redacted]`).

## 8. Commit details
- Commit message: **`Complete Terminal and file management mission`**
- Pushed to GitHub on `main` and verified online.

# Mission 3 — Understand the operating system

## 1. Task / objective
Explore the operating system from the Terminal: system details, current account, storage, running activity, processes, paths and file permissions. Explain the main responsibilities of an OS.

## 2. Work completed
- Collected OS details, account identity, storage and an activity snapshot (Task 3.1).
- Viewed the running process list, found the PID column and real examples (Task 3.2).
- Moved between folders to compare absolute and relative paths, and read the permission letters of a practice file (Task 3.3).
- Explained six OS responsibilities with my own examples (Task 3.4).
- Personal details (username, device name, disk ID) are replaced with `[redacted]`.

### Task 3.1 - Explore my operating system
Full output: [`evidence/mission-03-task3.1-output.txt`](../evidence/mission-03-task3.1-output.txt)

| Information explored | Command | What it tells me | My observation (privacy-safe) |
|----------------------|---------|------------------|-------------------------------|
| Operating system / system details | `uname -s -r -m`, `sw_vers` | The kernel name and version, the CPU architecture, and the macOS version. | Kernel **Darwin 27.2.0** on **arm64** (Apple Silicon). Product: **macOS 27.2.1**. |
| Current account identity | `whoami` | The name of the user account that is running the Terminal — this decides what files I am allowed to touch. | A normal (non-root) user account: `[redacted]`. |
| Available and used storage | `df -h /System/Volumes/Data` | Total size, used space, free space and % full of a disk, in human-readable units. | **926 GB** total, **397 GB** used, **504 GB** free, **45 %** full. (On macOS my files live on the *Data* volume; `/` alone is the read-only system volume.) |
| System activity snapshot | `top -l 1 -n 5 -o cpu` | A one-time snapshot of total processes, CPU load, memory use and the top processes. | **855 processes** in total (5 running, 850 sleeping), CPU about **65 % idle**, around **15 GB** of RAM in use. |

### Task 3.2 - Understand processes
I opened Google Chrome and then listed processes with `ps -ax -o pid,comm` (and also looked at `top`).
Full output: [`evidence/mission-03-task3.2-output.txt`](../evidence/mission-03-task3.2-output.txt)

| PID | Process | What it is |
|-----|---------|------------|
| 1 | `launchd` | The very first process macOS starts; it starts and manages all other processes. |
| 406 | `WindowServer` | Draws all the windows on the screen. |
| 708 | `Finder` | The file-manager app. |
| 21942 | `Google Chrome` | The browser I opened (Chrome also runs extra helper processes). |

- **What is a process?** A process is a program that is currently *running*. The app file on disk is just a program; when I open it, the OS loads it into memory, gives it CPU time and an ID — now it is a process. One app can create several processes (Chrome had more than one).
- **What does the PID column represent?** The **Process ID** — a unique number the OS gives each running process so it can track and control it (for example, `kill <PID>` would stop it). `launchd` always gets PID 1 because it starts first.
- **Two examples of processes running on my computer:** `Google Chrome` (an application I opened) and `WindowServer` (a background system process I never opened myself). In total `ps -ax | wc -l` counted about **854** processes.

### Task 3.3 - Paths and permissions
Full output: [`evidence/mission-03-task3.3-output.txt`](../evidence/mission-03-task3.3-output.txt)

Moving between folders:
```
$ cd mission-03-operating-system && pwd
/Users/[redacted]/.../digital-detective-8024/mission-03-operating-system
$ cd .. && pwd
/Users/[redacted]/.../digital-detective-8024
```
The current location changed to the subfolder and then back up one level.

- **Absolute path:** the full address starting from the root `/`. It works from anywhere.
  Example: `/Users/[redacted]/.../digital-detective-8024/mission-05-numbers-data/number_converter.py`
- **Relative path:** an address starting from *where I am right now*. It is shorter, but only works from the right folder.
  Example (from the repo root): `mission-05-numbers-data/number_converter.py` — or from inside `mission-03-operating-system`: `../mission-05-numbers-data/number_converter.py`

**Reading permissions** of my practice file:
```
$ ls -l mission-02-terminal/terminal-practice/notes.txt
-rw-r--r--@ 1 [redacted]  staff  82 Nov 15 03:39 notes.txt
```
Breaking down `-rw-r--r--`:

| Part | Letters | Meaning |
|------|---------|---------|
| File type | `-` | A normal file (`d` would mean directory). |
| Owner (me) | `rw-` | **Can read, can write, cannot execute.** |
| Group (`staff`) | `r--` | Can only read. |
| Others | `r--` | Can only read. |

The folder `terminal-practice` shows `drwxr-xr-x` — the owner has `rwx`, and the `x` on a directory means I am allowed to enter (`cd`) into it. The `@` at the end means macOS has extra attributes stored on the file. I did **not** change any permissions.

| Permission | Meaning | Example |
|------------|---------|---------|
| r - Read | Allows a file's contents to be read. | Opening `notes.txt` with `cat`. |
| w - Write | Allows a file to be changed. | Adding a line with `>>`. |
| x - Execute | Allows a file to be run; on a directory, allows access/traversal. | Running a script; `cd` into a folder. |

### Task 3.4 - Operating-system responsibilities

| OS responsibility | My explanation | Example |
|-------------------|----------------|---------|
| Process management | The OS starts and stops programs, gives each one a PID, and shares the CPU between them so many can run "at the same time". | I can play music in Chrome while typing in VS Code; `top` showed 850+ processes taking turns on the CPU. |
| Memory management | The OS decides which program gets which part of RAM, keeps programs from reading each other's memory, and moves data to disk (swap/compression) when RAM is full. | `top` showed 15 GB RAM used, part of it "compressed" — the OS squeezing memory when it ran low. |
| Device management | The OS talks to hardware through drivers so that apps don't need to know how each device works. | When I plug in earphones, sound switches to them automatically; the keyboard works in every app. |
| File management | The OS organises data into files and folders, tracks where each file is on the SSD, and handles create, copy, move and delete. | `mkdir`, `cp`, `mv` in Mission 2 — the OS did the real work on the disk. |
| User interface / shell | The OS gives a way for people to give instructions: a graphical interface (windows, Dock, Finder) and a text shell (Terminal running zsh). | I used the Terminal shell for this mission and Finder to see the same folders graphically. |
| Security and permissions | The OS checks who is logged in and what they are allowed to do, using accounts, passwords and r/w/x permissions. | My normal account can edit my own files (`rw-`) but cannot change system files without an admin password. |

## 3. Commands / tools used
| Command | Purpose |
|---------|---------|
| `uname -s -r -m` | Kernel name, version and CPU architecture. |
| `sw_vers` | macOS version. |
| `whoami` | Current account name (redacted in evidence). |
| `df -h` | Disk size, used and free space in readable units. |
| `top -l 1` | One snapshot of CPU, memory and top processes. |
| `ps -ax -o pid,comm` | List all processes with PID and name. |
| `grep` | Filter the process list to examples I wanted. |
| `wc -l` | Count the number of processes. |
| `cd`, `pwd` | Move between folders and see the path change. |
| `ls -l`, `ls -ld` | Read permission letters of a file / folder. |
| Activity Monitor | Graphical view of the same processes and PIDs. |

## 4. My understanding
The operating system is the "manager" sitting between the hardware and my apps. Every app I open becomes a process with its own PID; the OS shares the CPU and memory between hundreds of processes so smoothly that I never notice. Storage, paths and permissions are also controlled by the OS: paths are how I tell it *where* a file is (absolute = full address, relative = from here), and permissions are how it decides *who* may read, change or run that file. Seeing ~850 processes on a laptop where I had only a few apps open showed me how much the OS does in the background.

## 5. Difficulties faced
1. `df -h /` showed only about 13 GB used even though I know I have much more data on my Mac.
2. `top` normally keeps refreshing forever and fills the screen.

## 6. How I resolved them
1. I learned that on modern macOS, `/` is a small read-only **system** volume and my files are on a separate **Data** volume. Running `df -h /System/Volumes/Data` showed the real usage (397 GB).
2. I used `top -l 1` which takes just **one** sample and exits, and `-n 5` to show only 5 processes. (In normal `top`, pressing `q` quits.)

## 7. Evidence / files
- `evidence/mission-03-task3.1-output.txt` — OS, account, storage and activity snapshot.
- `evidence/mission-03-task3.2-output.txt` — process list with PIDs.
- `evidence/mission-03-task3.3-output.txt` — path changes and permission listing.

## 8. Commit details
- Commit message: **`Document operating system and file management`**
- Pushed to GitHub on `main` and verified online.

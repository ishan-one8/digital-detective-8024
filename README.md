# The Digital Detective 🔍

**Diwali Independent Learning Assignment — Explore Your Computer • Build a Mini System Report**

In this assignment I act as a "digital detective" and investigate my own computer: how it takes input and gives output, how the Terminal and the operating system work, how programs run, how numbers and text are stored as bits, how Git and GitHub track my work, and how computers talk to each other over a network.

The work is split into **missions**. Every mission has its own folder with its own `README.md`, and every mission was completed, committed and pushed separately before I started the next one.

## Mission index

| # | Mission | Folder |
|---|---------|--------|
| 0 | Repository and workspace setup | [mission-00-setup](mission-00-setup/README.md) |
| 1 | Computer fundamentals and IPOS | [mission-01-computer-basics](mission-01-computer-basics/README.md) |
| 2 | Terminal and file management | [mission-02-terminal](mission-02-terminal/README.md) |
| 3 | Operating system, processes and permissions | [mission-03-operating-system](mission-03-operating-system/README.md) |
| 4 | How programs run | [mission-04-programs](mission-04-programs/README.md) |
| 5 | Number systems, Python and text encoding | [mission-05-numbers-data](mission-05-numbers-data/README.md) |
| 6 | Git, GitHub, branches and Pull Requests | [mission-06-git-github](mission-06-git-github/README.md) |
| 7 | Computer networks | [mission-07-networking](mission-07-networking/README.md) |
| 8 | Final review and submission | [mission-08-final-report](mission-08-final-report/README.md) |

## My Learning

So far in this assignment I have learned that:

- **Every computer follows IPOS** — input, processing, output and storage — even "hidden" computers like ATMs and traffic lights.
- **The Terminal is powerful but needs care** — `>` replaces a whole file while `>>` only adds to the end, and pipes (`|`) let me join small commands into bigger tools.
- **Everything is stored as bits** — numbers, and even letters, are just binary patterns; hexadecimal is a short way to write 4 bits per digit, and UTF-8 lets text include characters like `₹`.

## Topics explored

- **Computer fundamentals** — IPOS cycle, hardware vs software, OS / application / utility software, everyday computer systems
- **Terminal** — `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `>` vs `>>`, flags (`-lah`), pipes (`|`), Homebrew
- **Operating system** — system info, storage, processes and PIDs, absolute vs relative paths, `rwx` permissions, OS responsibilities
- **How programs run** — running Python, compiler vs interpreter, bytecode
- **Data representation** — decimal, binary and hexadecimal conversions, Python verification, ASCII and UTF-8
- **Git & GitHub** — status, add, commit, log, branches, Pull Requests, merge and pull
- **Networking** — LAN/MAN/WAN, DNS, routers, protocols, packet switching, client-server, `ping` and `nslookup`

## Run the number converter

Requires Python 3.

```bash
cd mission-05-numbers-data
python3 number_converter.py
```

Then type a positive whole number, for example `25`:

```
Enter a positive decimal number: 25
Decimal     : 25
Binary      : 11001 (0b11001)
Hexadecimal : 19 (0x19)
```

## Summary of what I learned

This assignment changed how I see my laptop. I can now follow a key press all the way from the keyboard through the CPU and RAM to the screen and SSD, and I can see the hundreds of processes the operating system manages in the background. I am comfortable moving around and managing files in the Terminal, and I understand that all data — numbers and text — is just bits stored using agreed encodings. I learned to use Git properly: one meaningful commit per piece of work, branches for safe changes, and Pull Requests for review. Finally, I understand what really happens between typing a website name and seeing the page: DNS, routers, packets, protocols and the client-server model.

## How this repository was built

Each mission was finished, documented in its own README using the same 8-heading format, then **committed and pushed separately** before the next mission began. The commit history shows one dedicated commit per mission, plus the `update-about` branch and its merged Pull Request (#1) from Mission 6.

Privacy-safe outputs are kept in [`evidence/`](evidence/).

> Personal details (name, USN, computer username, device name, IP address, Wi-Fi name) are intentionally kept out of this public repository.

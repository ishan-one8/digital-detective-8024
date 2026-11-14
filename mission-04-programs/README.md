# Mission 4 - How programs run

## 1. Task / objective
Write and run a simple Python program, and compare how a **compiler** and an **interpreter** turn source code into something the computer can run.

## 2. Work completed
- Created [`hello.py`](hello.py) containing one line: `print("Hello from Python")`.
- Ran it from Terminal with Python 3 and confirmed the message appeared.
- Completed the compiler vs interpreter comparison table and wrote an explanation.

### Task 4.1 - Create and run a Python program
```bash
$ cd mission-04-programs
$ python3 hello.py
Hello from Python
```
The message appeared exactly as expected. Python version used: **3.14.5**.
Output saved in [`evidence/mission-04-hello-output.txt`](../evidence/mission-04-hello-output.txt).

### Task 4.2 - Compiler vs interpreter

| Point | Compiler | Interpreter |
|-------|----------|-------------|
| When translation / execution happens | The **whole program is translated first**, before it runs. Running is a separate, later step. | Code is translated and **executed while the program runs**, line by line / statement by statement. |
| Typical output | A separate **executable file** (machine code), e.g. `a.out` or `app.exe`, that can be run again without the source code. | **No separate executable** — you get the program's result directly. The source file is needed every time. |
| One example | **C** compiled with `gcc` / `clang`; also C++, Rust, Go. | **Python** (`python3 hello.py`); also JavaScript in a browser, Bash scripts. |
| One advantage | The finished program **runs faster**, and errors in syntax/types are caught before running. | **Quick to test and change** — edit and run immediately, with no build step; easy to try things in interactive mode. |

**Explanation:** A compiler and an interpreter both turn human-readable code into instructions the CPU can carry out — the difference is *when*. A compiler translates the whole program in advance and gives a standalone executable, so the program starts and runs fast, but every change needs a new compile. An interpreter, like the `python3` command I used, reads my `hello.py` and runs it on the spot, so I could write one line and see "Hello from Python" immediately, but it usually runs slower because translation happens during execution. In reality Python mixes both: it first compiles my code into **bytecode** (the `.pyc` files in `__pycache__`) and then its interpreter runs that bytecode.

## 3. Commands / tools used
| Command / tool | Purpose |
|----------------|---------|
| VS Code / `echo ... > hello.py` | Create the Python file. |
| `cd mission-04-programs` | Move into the mission folder. |
| `python3 hello.py` | Run the program using the Python 3 interpreter. |
| `python3 --version` | Confirm which Python version ran it. |
| `print()` | Python built-in function that displays text on the screen. |

## 4. My understanding
Computers only understand machine code (0s and 1s), so any program written in a language like Python or C must be translated. When I typed `python3 hello.py`, the OS started the Python interpreter as a process, the interpreter read my file, translated the `print` statement and asked the OS to show text in the Terminal — all in a fraction of a second. With a compiled language I would first run a compiler to produce an executable and then run that file. Knowing this explains why Python is great for learning and quick scripts, while compiled languages are often chosen for games and system software where speed matters most.

## 5. Difficulties faced
I was confused whether Python is "only" interpreted, because I read that Python also compiles code.

## 6. How I resolved them
I noticed that after running Python files a `__pycache__` folder with `.pyc` files can appear. I understood that Python compiles source into bytecode (not machine code) and then the interpreter runs that bytecode. So Python is mainly described as interpreted, but it uses both ideas — matching the assignment's note that real languages can combine both approaches. I added `__pycache__/` to `.gitignore` so these generated files are not committed.

## 7. Evidence / files
- `mission-04-programs/hello.py` — the working program.
- `evidence/mission-04-hello-output.txt` — Terminal output showing `Hello from Python`.

## 8. Commit details
- Commit message: **`Compare compilers and interpreters`**
- Pushed to GitHub on `main` and verified online.

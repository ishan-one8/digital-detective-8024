# Mission 1 - Know your computer

## 1. Task / objective
Explain how a computer receives input, processes it, produces output and stores the result (IPOS). Identify hardware and software I use, and find computer-based systems in everyday life.

## 2. Work completed
- Traced one real activity — **typing a note in a text editor and saving it** — through every IPOS stage (Task 1.1).
- Classified 5 hardware items and 5 software items I use, including the software type (Task 1.2).
- Listed 3 everyday computer-based systems with their purpose, one input and one output (Task 1.3).

### Task 1.1 - Trace one activity using IPOS
**Activity chosen:** typing a short note in VS Code on my MacBook and saving it as `notes.txt`.

| Stage | What happens in my example | Hardware / component |
|-------|----------------------------|----------------------|
| **Input** | I press keys on the keyboard. Each key press is turned into an electrical signal and a key code that is sent to the computer. I also click *File → Save* with the trackpad. | Keyboard, trackpad |
| **Processing** | The CPU receives each key code, the operating system passes it to VS Code, and VS Code works out which character to add and where. The text being typed is held in RAM (memory) while I work. When I save, the CPU converts the characters into bytes (UTF-8). | CPU (Apple M-series processor), RAM |
| **Output** | The GPU draws each new character on the screen almost instantly, so I can see what I typed. After saving, the tab title no longer shows the "unsaved" dot. | Display (screen), GPU |
| **Storage** | The bytes are written from RAM to the SSD as a file called `notes.txt`. The file stays there even after I shut down the laptop. | SSD (internal storage) |
| *Extra: Communication (optional)* | If iCloud sync is turned on, a copy of the file is also uploaded over Wi-Fi to cloud storage. | Wi-Fi card, cloud servers |

**How the activity flows:** my key presses are the **input**; the CPU and RAM **process** them into text in the editor; the screen shows the **output** straight away so I get feedback; and when I press Save, the text is moved from temporary memory (RAM, which forgets everything when the power goes off) into permanent **storage** on the SSD. RAM is fast but temporary, the SSD is slower but permanent — that is why "saving" is needed at all.

### Task 1.2 - Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
|----------------------|-----------------------|-------------------------------|---------|
| Keyboard | Hardware | Not applicable | Used to enter text and commands. |
| Trackpad | Hardware | Not applicable | Moves the pointer and clicks on things. |
| Display (screen) | Hardware | Not applicable | Shows output such as text, images and video. |
| SSD (internal storage) | Hardware | Not applicable | Keeps files and apps permanently, even when powered off. |
| Processor (CPU, Apple M-series) | Hardware | Not applicable | Carries out instructions and does all calculations. |
| macOS | Software | Operating system software | Manages hardware, memory, files and runs all other apps. |
| Google Chrome | Software | Application software | Browsing websites. |
| VS Code | Software | Application software | Writing and editing code and Markdown files. |
| Disk Utility | Software | Utility software | Checks, repairs and manages disks and storage. |
| Activity Monitor | Software | Utility software | Shows running processes, CPU and memory use; can stop frozen apps. |

### Task 1.3 - Computer systems around me

| System | Main purpose | One input | One output |
|--------|--------------|-----------|------------|
| ATM | Lets bank customers withdraw cash and check balance without a bank clerk. | Debit card + PIN typed on keypad | Cash notes and a printed receipt |
| Traffic signal (timer / sensor based) | Controls the flow of vehicles at a junction safely. | Timer count or vehicle sensor under the road | Red / yellow / green lights |
| Metro ticket / smart-card gate | Checks if a passenger has a valid ticket before letting them through. | Tapping a smart card or QR ticket on the reader | Gate opens and the screen shows the remaining balance |

## 3. Commands / tools used
| Tool | Purpose |
|------|---------|
| VS Code | Typed the note used for the IPOS example and wrote this README. |
| Activity Monitor / About This Mac | Looked at what hardware and software my Mac has. |
| Git (`git add`, `git commit`, `git push`) | Saved and published this mission. |

No special Terminal commands were needed for this mission.

## 4. My understanding
Every computer, from a laptop to an ATM, follows the same basic idea: **take input → process it → give output → store what is needed**. Hardware is the physical part you can touch; software is the set of instructions that tells the hardware what to do. Software itself has types: the **operating system** manages the whole computer, **application software** helps me do a task (browsing, coding), and **utility software** looks after the computer (checking disks, monitoring memory).

What surprised me is how many "hidden computers" exist around me — a traffic light or metro gate does not look like a computer, but it still has input, a processor, output and often storage.

## 5. Difficulties faced
At first I was not sure whether Activity Monitor and Disk Utility are application software or utility software, since both are apps I open like any other.

## 6. How I resolved them
I went back to the definitions in the assignment: utility software helps **maintain, protect or manage the computer itself**, while application software helps the **user do their own task**. Activity Monitor and Disk Utility manage the computer, so they are utilities; Chrome and VS Code help me do my work, so they are applications.

## 7. Evidence / files
- `mission-01-computer-basics/README.md` — this file with all three completed tables.

## 8. Commit details
- Commit message: **`Complete computer basics and IPOS mission`**
- Pushed to GitHub on `main` and verified online.

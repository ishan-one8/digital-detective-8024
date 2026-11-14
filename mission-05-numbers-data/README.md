# Mission 5 - Numbers and data

## 1. Task / objective
Convert numbers between decimal, binary and hexadecimal by hand, check the answers with Python, build a small number-converter program, and explain how text is stored using character encoding.

## 2. Work completed
- Did all 7 conversions by hand with full working (Task 5.1).
- Verified every answer in Python's interactive mode using `bin()`, `int(..., base)` and `hex()` — all matched (Task 5.2).
- Wrote [`number_converter.py`](number_converter.py) and tested it with 4 positive numbers plus 2 invalid inputs (Task 5.3).
- Found ASCII codes for `A` and `a` and explained encoding (Task 5.4).

> **Background:** a **bit** is a single 0 or 1. **8 bits = 1 byte.** Decimal is base 10 (digits 0-9), binary is base 2 (0-1), hexadecimal is base 16 (0-9 then A=10, B=11, C=12, D=13, E=14, F=15).

### Task 5.1 - Convert numbers by hand

**Method used:**
- *Decimal → binary:* keep dividing by 2, write down the remainders, then read them **from bottom to top**.
- *Binary → decimal:* multiply each bit by its place value (…8, 4, 2, 1) and add.
- *Hex → decimal:* multiply each digit by its place value (…256, 16, 1) and add.
- *Binary → hex:* split the bits into groups of 4 from the right; each group is one hex digit.

| Question | My working and answer |
|----------|-----------------------|
| Convert decimal **13** to binary. | 13 ÷ 2 = 6 r **1**<br>6 ÷ 2 = 3 r **0**<br>3 ÷ 2 = 1 r **1**<br>1 ÷ 2 = 0 r **1**<br>Read remainders bottom → top: **13 = 1101₂**<br>Check: 8 + 4 + 0 + 1 = 13 ✔ |
| Convert decimal **25** to binary. | 25 ÷ 2 = 12 r **1**<br>12 ÷ 2 = 6 r **0**<br>6 ÷ 2 = 3 r **0**<br>3 ÷ 2 = 1 r **1**<br>1 ÷ 2 = 0 r **1**<br>Bottom → top: **25 = 11001₂**<br>Check: 16 + 8 + 0 + 0 + 1 = 25 ✔ |
| Convert binary **1010** to decimal. | Place values 8 4 2 1<br>Bits         1 0 1 0<br>(1×8) + (0×4) + (1×2) + (0×1) = 8 + 0 + 2 + 0 = **10** |
| Convert binary **1101** to decimal. | Place values 8 4 2 1<br>Bits         1 1 0 1<br>(1×8) + (1×4) + (0×2) + (1×1) = 8 + 4 + 0 + 1 = **13** |
| Convert hexadecimal **A** to decimal. | A is a single hex digit in the 16⁰ = 1 place.<br>A = 10, so 10 × 1 = **10** |
| Convert hexadecimal **1F** to decimal. | Place values 16¹ = 16 and 16⁰ = 1<br>1 → 1 × 16 = 16<br>F → 15 × 1 = 15<br>16 + 15 = **31** |
| Convert binary **1111** to hexadecimal. | 1111 is already one group of 4 bits.<br>1111₂ = 8 + 4 + 2 + 1 = 15<br>15 in hex is **F**, so **1111₂ = F₁₆** |

### Task 5.2 - Verify using Python
I opened the interactive Python shell with `python3` and typed each expression.
Full session: [`evidence/mission-05-python-verification.txt`](../evidence/mission-05-python-verification.txt)

| Conversion type | Expression tested | Result | Matches my answer? |
|-----------------|-------------------|--------|--------------------|
| Decimal → binary | `bin(13)` | `'0b1101'` | ✅ Yes (1101) |
| Decimal → binary | `bin(25)` | `'0b11001'` | ✅ Yes (11001) |
| Binary → decimal | `int('1010', 2)` | `10` | ✅ Yes |
| Binary → decimal | `int('1101', 2)` | `13` | ✅ Yes |
| Hex → decimal | `int('A', 16)` | `10` | ✅ Yes |
| Hex → decimal | `int('1F', 16)` | `31` | ✅ Yes |
| Binary → hex | `hex(int('1111', 2))` | `'0xf'` | ✅ Yes (F) |
| Decimal → hex | `hex(31)` | `'0x1f'` | ✅ Yes (reverse check of 1F) |
| Decimal → hex | `hex(10)` | `'0xa'` | ✅ Yes (reverse check of A) |

Note: Python adds a prefix to show the base — `0b` means binary and `0x` means hexadecimal. The prefix is not part of the value.

### Task 5.3 - Number converter
**How the program works** ([`number_converter.py`](number_converter.py)):
1. `input()` shows a prompt and reads what the user types — always as **text** (a string).
2. `int()` converts that text into a whole number so maths can be done on it. If the text is not a number (e.g. `abc`), `int()` raises a `ValueError`, which I catch with `try/except` and print a friendly message. Negative numbers are also rejected.
3. `bin(number)` returns the number in base 2 as a string starting with `0b`.
4. `hex(number)` returns the number in base 16 as a string starting with `0x`.
5. I use slicing `[2:]` to remove the 2-character prefix, and `.upper()` to show hex letters in capitals, then `print()` both results.

**How to run it:**
```bash
cd mission-05-numbers-data
python3 number_converter.py
```
Example run:
```
=== Digital Detective Number Converter ===
Enter a positive decimal number: 25
Decimal     : 25
Binary      : 11001 (0b11001)
Hexadecimal : 19 (0x19)
```

**Test results** (full output in [`evidence/mission-05-converter-tests.txt`](../evidence/mission-05-converter-tests.txt)):

| Test number | Binary output | Hexadecimal output |
|-------------|---------------|--------------------|
| 13 | 1101 | D |
| 25 | 11001 | 19 |
| 255 | 11111111 | FF |
| 2026 | 11111101010 | 7EA |
| `abc` (invalid) | "That is not a whole number…" | — |
| `-5` (invalid) | "Please enter a positive number…" | — |

The outputs for 13 and 25 match my hand working from Task 5.1. 255 = `11111111` is the biggest number that fits in **one byte** (8 bits all 1), which is `FF` in hex — this shows why one hex digit represents exactly 4 bits.

### Task 5.4 - How is text stored?
- **ASCII codes:** uppercase **`A` = 65**, lowercase **`a` = 97** (checked with `ord('A')` and `ord('a')` in Python). Upper and lower case differ by exactly 32.
- **Why an encoding standard is needed:** a computer can only store numbers (bits), not letters. An encoding standard is an agreed table that says which number stands for which character, so that text saved on one computer shows the same letters when opened on another.
- **A character that is not in basic ASCII:** the Indian Rupee sign **`₹`**. ASCII only has 128 characters (codes 0-127), but `ord('₹')` is **8377**. In UTF-8 it is stored as **3 bytes** (`e2 82 b9`), while `A` is stored as just 1 byte (the same as ASCII). Hindi letters like `अ` and emojis like `🪔` are also outside ASCII.

## 3. Commands / tools used
| Command / function | Purpose |
|--------------------|---------|
| `python3` | Open Python's interactive shell (`>>>`) for verification; `exit()` to leave. |
| `python3 number_converter.py` | Run the converter program. |
| `bin(n)` | Decimal integer → binary string (`0b…`). |
| `hex(n)` | Decimal integer → hexadecimal string (`0x…`). |
| `int(text)` | Text → integer (base 10). |
| `int(text, 2)` / `int(text, 16)` | Read text as a binary / hexadecimal number and give its decimal value. |
| `input()`, `print()` | Read from and write to the user. |
| `ord(ch)` | Give the code number of a character. |
| `str.encode('utf-8')` | Show the actual bytes used to store text in UTF-8. |

## 4. My understanding
Everything in a computer — numbers, text, images — is stored as patterns of bits. Binary is the computer's natural language because a circuit can easily be *on* (1) or *off* (0). Hexadecimal is a short, human-friendly way of writing binary: every hex digit is exactly 4 bits, so one byte is always two hex digits (e.g. `11111111` = `FF`). Text works the same way: each character is given a number by an encoding (ASCII for basic English, UTF-8 for almost every language and emoji), and that number is stored in binary. UTF-8 is clever because English letters still take only 1 byte, while other characters use 2-4 bytes.

## 5. Difficulties faced
1. In decimal → binary I first read the remainders from top to bottom and got 1011 for 13, which is wrong.
2. Python's results had `0b` and `0x` in front, so at first they did not look like my answers.
3. When I first wrote the converter, typing letters made the program crash with `ValueError`.

## 6. How I resolved them
1. I checked by converting back (1011₂ = 11, not 13) and realised the remainders must be read **bottom to top**. After that, 13 = 1101 ✔.
2. I learned these are just prefixes that show the base. I removed them in my program with `[2:]`.
3. I wrapped `int()` in a `try/except ValueError` block so the program prints a helpful message instead of crashing, and added a check for negative numbers.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py` — the working converter.
- `evidence/mission-05-python-verification.txt` — Python verification expressions and results.
- `evidence/mission-05-converter-tests.txt` — converter test runs. (In this saved log the numbers were sent to the program through a pipe, so the typed number shows as "(typed: …)" instead of appearing after the prompt.)

## 8. Commit details
- Commit message: **`Build number converter and practise data representation`**
- Pushed to GitHub on `main` and verified online.

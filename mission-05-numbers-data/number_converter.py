# Number Converter - The Digital Detective, Mission 5
# Asks for a decimal number and shows it in binary and hexadecimal.

print("=== Digital Detective Number Converter ===")

text = input("Enter a positive decimal number: ")

try:
    number = int(text)          # turn the typed text into an integer
except ValueError:
    print("That is not a whole number. Please run the program again.")
else:
    if number < 0:
        print("Please enter a positive number (0 or more).")
    else:
        binary = bin(number)    # e.g. 13 -> '0b1101'
        hexa = hex(number)      # e.g. 31 -> '0x1f'

        print("Decimal     :", number)
        print("Binary      :", binary[2:], f"({binary})")
        print("Hexadecimal :", hexa[2:].upper(), f"({hexa})")

Task 5.1

13 into decimal -
13 / 2 = 6 remainder 1, 6 / 2 = 3 remainder 0, 3 / 2 = 1 remainder 1, 1 / 2 = 0 remainder 1. Reading remainders bottom-to-top gives 1101.

25 to binary -
25 / 2 = 12 remainder 1, 12 / 2 = 6 remainder 0, 6 / 2 = 3 remainder 0, 3 / 2 = 1 remainder 1, 1 / 2 = 0 remainder 1. Reading remainders bottom-to-top gives 11001.

1010 to decimal -
(1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (0 * 2^0) = 8 + 0 + 2 + 0 = 10.

1101 to decimal - 
(1 * 2^3) + (1 * 2^2) + (0 * 2^1) + (1 * 2^0) = 8 + 4 + 0 + 1 = 13.

A to decimal - 
In base 16, A = 10

1F to decimal -
(1 * 16^1) + (15 * 16^0) = 16 + 15 = 31 (since F = 15).

1111 to hexadecimal -
(1 * 8) + (1 * 4) + (1 * 2) + (1 * 1) = 15, which is F in hexadecimal.

Task 5.2

This is a copy paste from my terminal,(it began with "python3", the ">>>" are my inputs and the line under them are the outputs and it ended in "exit()")

python3

>>> bin(13)
'0b1101'
>>> bin(25)
'0b11001'
>>> int('1010', 2)
10
>>> int('1101', 2)
13
>>> int('A', 16)
10
>>> int('1F', 16)
31
>>> hex(int('1111', 2))
'0xf'
>>> exit()

Task 5.3

The test cases with the outputs shown in the result part

13
Binary: 0b1101 (without prefix: 1101)
Hexadecimal: 0xd (without prefix: D)

25
Binary: 0b11001 (without prefix: 11001)
Hexadecimal: 0x19 (without prefix: 19)

10001
Binary: 0b10011100010001 (without prefix: 10011100010001)
Hexadecimal: 0x2711 (without prefix: 2711)

bin() (Binary conversion): Converts a decimal integer into its base-2 string representation using only 0 and 1 digits (representing powers of 2), prefixed with 0b

hex() (Hexadecimal conversion): Converts a decimal integer into its base-16 string representation using digits 0–9 and letters A–F (representing powers of 16), prefixed with 0x.

Task 5.4

ASCII decimal codes: Uppercase A = 65, lowercase a = 97

Computers only store binary numbers (0s and 1s), so a shared encoding standard maps every character to a specific numeric code so different devices and programs display the exact same text consistently.

Any emoji non-english script character (like Hindi or Kannada) requires Unicode / UTF-8.

Mission 5 - Numbers and data

1. Task / objective
Convert numbers manually between decimal, binary, and hexadecimal systems with step-by-step working, verify all calculations in Python, build an interactive "number_converter.py" program, and explain how text is stored using ASCII and UTF-8 character encoding.

2. Work completed
- Completed Task 5.1 by solving seven decimal, binary, and hexadecimal conversion problems by hand with step-by-step division and positional power calculations.
- Completed Task 5.2 by testing and verifying every manual result in the interactive Python 3 shell.
- Completed Task 5.3 by building "mission-05-numbers-data/number_converter.py", testing it with three positive decimal numbers ("13", "42", and "255"), and explaining how "bin()" and "hex()" work.
- Completed Task 5.4 by recording the ASCII decimal codes for "A" ("65") and "a" ("97"), explaining why encoding standards are necessary, and identifying non-ASCII characters supported by UTF-8.

3. Commands / tools used
- "python3" (interactive shell) — Verified manual conversions using "bin()", "hex()", and "int(..., base)".
- "python3 mission-05-numbers-data/number_converter.py" — Executed the number converter script across three test inputs.
- "input()", "int()", "bin()", "hex()", and "ord()" — Python built-in functions used to read user input, convert bases, and inspect ASCII character codes.
- "git add", "git commit", and "git push" — Staged, committed, and pushed Mission 5 to GitHub.

4. My understanding
Computers store all numbers and text in binary ("0"s and "1"s). Binary (base 2) maps directly to hardware states, while hexadecimal (base 16) provides a compact, human-readable shorthand where every hex digit represents four binary bits. Prefixes like "0b" and "0x" distinguish number bases in code, and character-encoding standards like ASCII and UTF-8 map numeric codes to text characters so different systems display text consistently.

5. Difficulties faced
No major difficulties.

6. How I resolved them
Not applicable.

7. Evidence / files
- "mission-05-numbers-data/number_converter.py"
- "mission-05-numbers-data/README.md" (containing Task 5.1 manual calculations, Task 5.2 Python verification table, Task 5.3 converter test runs, and Task 5.4 ASCII/UTF-8 notes)

8. Commit details
Committed with message "Build number converter and practise data representation" and pushed to "master" on GitHub.

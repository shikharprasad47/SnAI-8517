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
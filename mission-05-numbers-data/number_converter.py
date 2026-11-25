number = int(input())

binary_value = bin(number)
hex_value = hex(number)

print(f"Binary: {binary_value} (without prefix: {binary_value[2:]})")
print(f"Hexadecimal: {hex_value} (without prefix: {hex_value[2:].upper()})")
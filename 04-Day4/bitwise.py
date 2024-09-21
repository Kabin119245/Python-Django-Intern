a = 5  # binary: 101
b = 3  # binary: 011

# Bitwise AND
and_result = a & b  # Output: 1 (binary: 001)

# Bitwise OR
or_result = a | b  # Output: 7 (binary: 111)

# Bitwise XOR
xor_result = a ^ b  # Output: 6 (binary: 110)

# Bitwise NOT
not_result = ~a  # Output: -6 (binary: ~101 = ...111111010)

# Left Shift
left_shift = a << 1  # Output: 10 (binary: 1010)

# Right Shift
right_shift = a >> 1  # Output: 2 (binary: 10)

print(f"AND: {and_result}, OR: {or_result}, XOR: {xor_result}, NOT: {not_result}, "
      f"Left Shift: {left_shift}, Right Shift: {right_shift}")

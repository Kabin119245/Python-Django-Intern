# Write a program to find the frequency of each character
# in a string.

str = input("Enter any string: ")

freq = {}

for char in str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for char, count in freq.items():
    print(f"'{char}': {count}")

# Write a Python program that counts how many times
# each vowel appears in a given string.

str = input("Enter any string: ")

vowels = 'aeiouAEIOU'

freq = {vowel : 0 for vowel in vowels}

for char in str:
    if char in vowels:
        freq[char] += 1

for vowel, count in freq.items():
    if count > 0:
        print(f"'{vowel}': {count}")

# print(freq)

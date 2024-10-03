# Write a Python program that checks if a string contains
# only alphabets (no digits or special characters).

s = input("Enter any string: ")

contains_only_alphabets = True

for char in s:
    if not char.isalpha():
        contains_only_alphabets = False
        break

if contains_only_alphabets:
    print("Your string contains only alphabets")
else:
    print("Your string does not contain only alphabets")

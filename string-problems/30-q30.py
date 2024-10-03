# Write a Python program that checks if a string starts
# and ends with the same character.


str = input("Enter any string: ")

if str[0] == str[-1]:
    print("They start and end with same character")
else:
    print("They don't start and end with same character")
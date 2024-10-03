# Write a Python program that checks if a string contains
# only alphabets (no digits or special characters).

str = input("Enter any string: ")

if(str.isalpha()):
    print("Your string contains only alphabets")
else:
    print("Your string  does not contain only alphabets")
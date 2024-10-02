# Write a Python program that asks the user to input a string
# and then outputs the string in reverse.

def reverse(str):
    s = "";
    for i in str:
        s = i + s
    return s

s = input("Enter any string: ")
print("The original string is : ")
print(s)

print("The reversed string(using loops) is : ")
print(reverse(s))
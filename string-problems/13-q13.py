# Write a program to compare two strings
# lexicographically and determine which one comes first
# alphabetically.

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if string1 < string2:
        print( f"'{string1}' comes before '{string2}' alphabetically.")
elif string1 > string2:
        print( f"'{string2}' comes before '{string1}' alphabetically.")
else:
        print( f"'{string1}' and '{string2}' are the same.")
        
        
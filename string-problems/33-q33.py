# Write a Python program that finds and prints the
# longest repeated substring in a given string. 
# Input the string
str= input("Enter a string: ")
n = len(str)
longest = ""


for i in range(n):
    for j in range(i + 1, n + 1):
        substring = str[i:j]
        
        if str.count(substring) > 1 and len(substring) > len(longest):
            longest = substring

if longest:
    print("The longest repeated substring is:", longest)
else:
    print("No repeated substring found.")

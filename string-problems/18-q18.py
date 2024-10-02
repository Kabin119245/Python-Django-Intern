# Write a program to count the number of words in a
# string. 

str = input("Enter a sentence: ").rstrip()

words = str.split()
wc = len(words)

print(f"The number of words in the string is: {wc}")
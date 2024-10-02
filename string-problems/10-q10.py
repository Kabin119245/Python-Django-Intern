# Write a Python program that finds all occurrences of
# the letter 'a' in the string "banana" and prints their positions. 

string = "banana"
char = 'a'

positions = []

for i in range(len(string)):
    if string[i] == char:
        positions.append(i)
        
if positions:
    print(f"The letter '{char}' is found at positions: {positions}")
else:
    print(f"The letter '{char}' is not found in the string.")

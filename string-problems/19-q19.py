# Write a program to remove duplicate characters from a
# string while preserving the order of characters. 

str = input("Enter any string: ")

result = ""
seen = []

for char in str:
    if char not in seen:
        result = result + char
        seen.append(char)
        
print(f"String after removing duplicates: {result}")
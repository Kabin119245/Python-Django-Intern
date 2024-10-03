# Write a program to find the shortest word in a string. 

str = input("Enter a string: ")

words = str.split()

shortest_word = words[0]
min_length = len(words[0])

for word in words:
    if len(word) < min_length:
        shortest_word = word
        min_length = len(word)


print(f"The longest word is: {shortest_word}")

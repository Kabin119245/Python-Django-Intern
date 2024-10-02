str = input("Enter a string: ")

words = str.split()

longest_word = ""
max_length = 0

for word in words:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)


print(f"The longest word is: {longest_word}")

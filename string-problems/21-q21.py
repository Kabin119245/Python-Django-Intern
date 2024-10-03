# Write a program that splits a string by commas and
# then sorts each word in alphabetical order.

s = 'apple, banana, orange, mango, grapes'
words = s.split(",")

words = [word.strip() for word in words]
words.sort()

print(words)


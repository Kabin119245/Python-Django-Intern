# Write a Python program to convert a string from
# snake_case to camelCase. 

str = input("Enter string in snake case, example(hi_i_am_python): " )

words = str.split('_')

camel_str = words[0].lower() + ''.join(word.capitalize() for word in words[1:])

print(camel_str)
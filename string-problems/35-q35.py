# Write a Python program to replace every second
# character of a string with *.

s = input("Enter any string: ")
s_list = list(s)


for i in range(1, len(s_list), 2):
    s_list[i] = '*'

modified_string = ''.join(s_list)

print("Modified string:", modified_string)



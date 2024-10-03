# Write a program that checks if a string contains any
# numeric characters. 

str = input("Enter any string: ")

contains_num = False

for char in str:
    if(char.isnumeric()):
        contains_num = True
        break
        
if contains_num:
    print("Contains numeric character")
else:
    print("Does not contain numeric character")
my_string = input("Enter any string: ")  

if my_string == my_string[::-1]:
    print(f"{my_string} is a palindrome string")
else:
    print(f"{my_string} is not a palindrome string")
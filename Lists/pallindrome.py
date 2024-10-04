my_list = [10, 20, 30, 20, 10]

if list(reversed(my_list)) == my_list:
# if mylist == mylist[::-1]
     print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")


my_list = [10, 20, 30, 20, -10]

if list(reversed(my_list)) == my_list:
# if mylist == mylist[::-1]
     print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

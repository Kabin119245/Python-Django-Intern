# Check if a given string is a palindrome (reads the same
# backward as forward). 

def reverse(str):
    s = "";
    for i in str:
        s = i + s
    return s

input_string = input("Enter any string: ")

reversed_string = reverse(input_string)

if(input_string == reversed_string):
    print("It is pallindrome string")
else:
    print("Not a pallindrome word")
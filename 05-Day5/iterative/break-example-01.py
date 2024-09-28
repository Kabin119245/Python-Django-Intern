# Program to demonstrate break statement

print("Enter numbers to continue. Enter 0 to exit.")

while True:
    user_input = input("Enter a number: ")

    # Check if the user wants to exit
    if user_input == '0':
        break  # Exit the loop if the input is 0

    print(f"You entered: {user_input}")

print("Exited the loop.")

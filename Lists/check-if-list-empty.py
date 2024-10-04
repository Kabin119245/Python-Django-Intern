
my_list = []

# 1. Using if statement directly 
if not my_list:
    print("Method 1: The list is empty.")
else:
    print("Method 1: The list is not empty.")

# 2. Using len() function
if len(my_list) == 0:
    print("Method 2: The list is empty.")
else:
    print("Method 2: The list is not empty.")

# 3. Comparing with an empty list []
if my_list == []:
    print("Method 3: The list is empty.")
else:
    print("Method 3: The list is not empty.")
    
my_list = [10,20]

if not my_list:
    print(" The list is empty.")
else:
    print(" The list is not empty.")

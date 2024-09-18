Var = ["I","LOVE","NEPAL"]
print(Var)
print(type(Var))


# 1. Create a list
my_list = [1, 2, 3, 4, 5, "Nepal", True, 5+2j]

# 2. Access elements
print("First element:", my_list[0])   # Access the first element
print("Last element:", my_list[-1])   # Access the last element

# 3. Modify an element
my_list[2] = 10   # Modify the third element
print("Modified list:", my_list)

# 4. Append an element
my_list.append(6)   # Add an element to the end of the list
print("List after appending:", my_list)

# 5. Remove an element
my_list.remove(4)   # Remove the element '4'
print("List after removing 4:", my_list)

# 6. Length of the list
print("Length of the list:", len(my_list))

# 7. Insert an element at a specific index
my_list.insert(1, 20)  # Insert '20' at index 1
print("List after insertion:", my_list)


# 9. Reverse the list
my_list.reverse()
print("Reversed list:", my_list)


# 10. Slicing
print(my_list[2:5])

var = ("My", "name", "is","Khan")
print(var)
print(type(var))
# 1. Create a tuple
my_tuple = (1, 2, 3, 4, 5, "Nepal", True, 5+2j)
print("Original tuple:", my_tuple)

# 2. Access elements
print("First element:", my_tuple[0])   # Access the first element
print("Last element:", my_tuple[-1])   # Access the last element

# 3. Find length of tuple
print("Length of the tuple:", len(my_tuple))

# 4. Count occurrences of an element
print("Count of 3 in tuple:", my_tuple.count(3))

# 5. Find index of an element
print("Index of element 4:", my_tuple.index(4))
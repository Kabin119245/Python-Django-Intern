# 1. Create a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# 2. Add an element to the set
my_set.add(6)   # Add element 6
print("Set after adding 6:", my_set)

# 3. Remove an element from the set
my_set.remove(4)   # Remove element 4 (raises error if element doesn't exist)
print("Set after removing 4:", my_set)

# 4. Check if an element exists in the set
print("Is 3 in the set?", 3 in my_set)

# 5. Get the length of the set
print("Length of the set:", len(my_set))

# 6. Use set operations (union, intersection, difference)
another_set = {3, 5, 7, 8}

# Union: combines both sets
union_set = my_set.union(another_set)
print("Union of sets:", union_set)

# Intersection: common elements between both sets
intersection_set = my_set.intersection(another_set)
print("Intersection of sets:", intersection_set)

# Difference: elements in my_set but not in another_set
difference_set = my_set.difference(another_set)
print("Difference of sets:", difference_set)

# 7. Clear the set
my_set.clear()  # Removes all elements
print("Set after clearing:", my_set)

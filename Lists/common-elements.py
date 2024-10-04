list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = [x for x in list1 if x in list2]
print("Common elements using list comprehension:", common_elements)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = list(set(list1) & set(list2))

print("Common elements using set intersection:", common_elements)

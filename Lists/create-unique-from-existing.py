# Original list with duplicates
my_list = [10, 20, 20, 30, 40, 40, 50, 50, 50]

unique_list = list(set(my_list))
print("Unique elements using set():", unique_list)


new_list = []

for item in my_list:
    if item not in new_list:
        new_list.append(item)
print("Unique elements using for loop:", unique_list)


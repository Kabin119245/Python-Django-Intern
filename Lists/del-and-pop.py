# Original list
my_list = [100, 200, 300, 400, 500]

del my_list[2]
print("After deletion using del:", my_list)

removed_element = my_list.pop(1)
print("After deletion using pop:", my_list)
print("Removed element using pop:", removed_element)

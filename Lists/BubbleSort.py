my_list = [10, 20, 30, 2, 100,3, -2]

for i in range(len(my_list)):
    for j in range(0, len(my_list)-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(f"Sorted list is: ", my_list)
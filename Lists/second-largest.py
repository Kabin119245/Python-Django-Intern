my_list = [10, 20, 30, 2, 100,3, -2,90]

for i in range(len(my_list)):
    for j in range(0, len(my_list)-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

l2 = my_list[::-1]
del l2[0]
print(f"The second largest element is: ",l2[0])
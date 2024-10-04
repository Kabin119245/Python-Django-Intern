my_list = [10,20,"Kabin", "Shyam", 10.20, 5.5, [90,80,70]]

#positive slicing
sliced_list = my_list[1:4]
print(sliced_list)

print(my_list[6:])

#negative slicing

print(my_list[-3:])

#we can also reverse list using slicing
reversed_list = my_list[::-1]
print(reversed_list)

#using steps:
print(my_list[1:-1:2])
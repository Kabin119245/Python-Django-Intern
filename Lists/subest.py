list1 = [10,20,30,40,50,60,70]
list2 = [10,20,30,40,50,60,70,60,70,80,90,100]

is_subset = True

for item in list1:
    if item not in list2:
        is_subset = False
        break
if is_subset:
    print("list1 is a subset of list2")
else:
    print("list1 is not a subset of list2")
        

        
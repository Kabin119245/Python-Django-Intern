list1 = [10,20,30,40,50]
list2 = [60,70,80,90,100]

list3 = []
i=0
j=0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        list3.append(list1[i])
        i = i + 1
    else:
        list3.append(list2[j])
        j = j + 1

list3.extend(list1[i:])
list3.extend(list2[j:])

print(f"Merged Sorted List is: ", list3)
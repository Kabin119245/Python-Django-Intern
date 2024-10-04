
lists = [[1, "Kabin"], ["Shyam", 4], [5, "Hari", "Gita"]]


flat_list = []

for sublist in lists:
    for item in sublist:
        flat_list.append(item)

print("Flattened list:", flat_list)

lst = [1, 2, 3, 4, 5, 6]
target_sum = 9

pairs = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target_sum:
            pairs.append((lst[i], lst[j]))

print("Pairs: ", pairs)

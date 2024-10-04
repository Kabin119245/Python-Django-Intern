nums= [9, 4, 7, 1, 3, 2,3,4, 5, 6, 10, 8, 9,1000]

num_set = set(nums)

max_length = 0
longest_sequence = []

for num in num_set:
  if num - 1 not in num_set:  
    current_num = num
    current_length = 1
    current_sequence = [num]

    while current_num + 1 in num_set:
      current_num += 1
      current_length += 1
      current_sequence.append(current_num)

    if current_length > max_length:
      max_length = current_length
      longest_sequence = current_sequence 


print("Longest sequence length:", max_length)
print("Longest sequence:", longest_sequence)
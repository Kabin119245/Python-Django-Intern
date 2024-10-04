nums= [9, 4,2,2,2,2,2, 7, 1, 3, 2,3,4, 5, 6, 10, 8, 9,1000, 2,2,2,2,2,2,2,2,2,2]

candidate = None

count = 0
for num in nums:
    if count == 0:
        candidate = num  
    if num == candidate:
        count = count + 1
    else:
        count -= 1

if nums.count(candidate) > len(nums) // 2:
    print(f"The majority element is: {candidate}")
else:
    print("No majority element found.")
    
    
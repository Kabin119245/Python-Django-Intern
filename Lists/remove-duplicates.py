l = [1,1,2,3,3,4,5,6,6,8]

seen = set()
result = []

for item in l:
    if item not in seen:
        result.append(item)
        seen.add(item)
        
print(f"List without duplicates with original order: ", result)
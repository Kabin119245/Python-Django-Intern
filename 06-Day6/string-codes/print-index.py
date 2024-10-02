my_string = "My country's name is Nepal"
i=0
print("---Index of every characters in both positive and negative---")
for x in my_string:
    print(f"The character {x} is present at positive {i} index and negative index {i - len(my_string)}")
    i += 1
    
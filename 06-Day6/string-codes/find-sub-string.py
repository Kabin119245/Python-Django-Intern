
text = "Python programming is fun and programming is great"

# Using find()
find_position = text.find("programming")
print("Using find():", find_position)  # Output: 7
print("Position of 'Java':", text.find("Java"))  # Output: -1

# Using index()
index_position = text.index("programming")
print("\nUsing index():", index_position)  # Output: 7
# print(text.index("Java"))  # This line would raise ValueError if uncommented

# Using rfind()
rfind_position = text.rfind("programming")
print("\nUsing rfind():", rfind_position)  # Output: 30
print("Last position of 'Java':", text.rfind("Java"))  # Output: -1

# Using rindex()
rindex_position = text.rindex("programming")
print("\nUsing rindex():", rindex_position)  # Output: 30
# print(text.rindex("Java"))  # This line would raise ValueError if uncommented

# Integer comparison
a = 10
b = 50
print("Integer comparison:")
print(a == b)  # False
print(a != b)  # True

x = 2
y = 2
print(a == b)  # True
print(a != b)  # False

# Float comparison
x = 10.5
y = 20.5
print("\nFloat comparison:")
print(x == y)  # False
print(x != y)  # True

# String comparison
str1 = "hello"
str2 = "world"
print("\nString comparison:")
print(str1 == str2)  # False
print(str1 != str2)  # True

# Boolean comparison
bool1 = True
bool2 = False
print("\nBoolean comparison:")
print(bool1 == bool2)  # False
print(bool1 != bool2)  # True

# Comparison between boolean and integer
bool_int1 = True  # True is treated as 1
bool_int2 = False  # False is treated as 0
print("\nBoolean and Integer comparison:")
print(bool_int1 == 1)  # True (True is equivalent to 1)
print(bool_int2 == 0)  # True (False is equivalent to 0)
print(bool_int1 != 0)  # True (True is not 0)
print(bool_int2 != 1)  # True (False is not 1)

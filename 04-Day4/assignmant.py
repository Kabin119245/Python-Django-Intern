# Integer and float operations
a = 15        # integer
b = 2.5       # float

print(f"Initial a (int): {a}, b (float): {b}")
a += b        # addition assignment (int + float)
print(f"After a += b: {a}")

a -= 5.5      # subtraction assignment (int - float)
print(f"After a -= 5.5: {a}")

a *= 2        # multiplication assignment (int * int)
print(f"After a *= 2: {a}")

b /= 2        # division assignment (float / int)
print(f"After b /= 2: {b}\n")

# String operations
str1 = "Hello"
str2 = " World"

print(f"Initial str1: {str1}, str2: {str2}")
str1 += str2   # string concatenation
print(f"After str1 += str2: {str1}")

# str1 *= 2     # string repetition
print(f"After str1 *= 2: {str1 * 2}\n")

# List operations
list1 = [1, 2, 3]
list2 = [4, 5]

print(f"Initial list1: {list1}, list2: {list2}")
list1 += list2  # list concatenation
print(f"After list1 += list2: {list1}")

list1 *= 2      # list repetition
print(f"After list1 *= 2: {list1}\n")

# Modulus operation on integers
x = 20
print(f"Initial x: {x}")
x %= 6  # remainder assignment
print(f"After x %= 6: {x}\n")

# Exponentiation
y = 3
print(f"Initial y: {y}")
y **= 4  # exponentiation assignment
print(f"After y **= 4: {y}\n")





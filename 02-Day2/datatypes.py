# Integer (int)
a = 10
print("Integer:")
print("Value:", a, "| Type:", type(a))

# Float (float)
b = 3.14
print("\nFloat:")
print("Value:", b, "| Type:", type(b))

# String (str)
c = "Hello"
print("\nString:")
print("Value:", c, "| Type:", type(c))

# Boolean (bool)
d = True
print("\nBoolean:")
print("Value:", d, "| Type:", type(d))

# Operations between them:

# Arithmetic Operations
print("\nArithmetic Operations:")
print(f"Addition (int + float): {a} + {b} = {a + b}")  # int + float
print(f"Multiplication (int * float): {a} * {b} = {a * b}")  # int * float
print(f"Division (float / int): {b} / {a} = {b / a}")  # float / int

# String Operations
print("\nString Operations:")
print(f"Concatenation: {c} + ' World' = {c + ' World'}")  # string concatenation
print(f"Repetition: {c} * 3 = {c * 3}")  # string repetition

# Boolean Operations
print("\nBoolean Operations:")
print(f"Boolean AND: {d} and False = {d and False}")  # boolean AND
print(f"Boolean OR: {d} or False = {d or False}")  # boolean OR
print(f"Boolean NOT: not {d} = {not d}")  # boolean NOT

# Combined Operations
print("\nCombined Operations:")
print(f"String and Boolean: {c + ' is ' + str(d)}")  # Concatenate string with boolean (after converting boolean to string)
print(f"String and Arithmetic: {c + ' ' + str(a + b)}")  # Concatenate string with the result of arithmetic operation


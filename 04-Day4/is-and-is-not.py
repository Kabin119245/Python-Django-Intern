x = 100
y = 200
print(id(x))
print(id(y))
print(x is y)

x = 100
y = 100
print(id(x))
print(id(y))
print(x is y)

a = [1, 2, 3]  
b = [1, 2, 3]  
c = a         

print(a is b)  
print(a is c) 

# Example of `is not` operator
print(a is not b)  
print(a is not c) 

# Example with `None`
x = None
y = None

print(x is None)  # True, both x and None refer to the same None object
print(y is not None)  # False, y is None

# Example with integers (note: small integers may share memory)
x = 1000
y = 1000

print(x == y)  
print(x is y) 

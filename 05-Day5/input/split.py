# Input multiple values separated by spaces
name, age, city = input("Enter your name, age, and city (separated by spaces): ").split()

print("Name:", name)
print("Age: ", age)
print("City: ", city)




numbers = [int(n) for n in input("Enter numbers separated by spaces: ").split()]

print("Numbers:", numbers)

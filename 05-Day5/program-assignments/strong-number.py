import math

n = input("Enter any integer number: ")
sum = 0
original = int(n)

for digit in n:
    sum += math.factorial(int(digit))

if sum == original:
    print(f"{n} is a Strong number")
else:
    print(f"{n} is not a Strong number")


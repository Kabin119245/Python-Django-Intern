num = int(input("Enter any integer number"))

digits = len(str(num))
sum = 0
original = num

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num //10

if sum == original:
    print(f"{original} is an Armstrong number")
else:
    print(f"{original} is not an Armstrong number")
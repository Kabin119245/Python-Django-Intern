num = int(input("Enter any integer number: "))

a = 0
b = 1
if num == a or num == b:
    print(f"{num} is a Fibonacci number")
else:
    while b < num:
        a,b = b, a+b
        
    if b == num:
        print(f"{num} is a Fibonacci number")
    else:
        print(f"{num} is not a Fibonacci number")




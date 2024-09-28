n = int(input("Enter the number of terms: "))
a = 0 
b = 1
if n == 1:
    print(f"Fibonacci series up to {n} term: {a}")
else:
    for i in range(n):
        print(a, end=" ")
        temp = a
        a = b
        b = temp + b
# a, b = b, a+b
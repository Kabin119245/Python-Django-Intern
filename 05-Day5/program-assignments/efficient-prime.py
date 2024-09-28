import math

n = int(input("Enter any integer number: "))

if n <= 1:
    print(f"{n} is not a prime number")
elif n <= 3:
    print(f"{n} is a prime number")
elif n % 2 == 0 or n % 3 == 0:
    print(f"{n} is not a prime number")
else:
    is_prime = True
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

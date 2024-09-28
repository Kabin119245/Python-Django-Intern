
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


if is_prime(num1) and is_prime(num2) and abs(num1 - num2) == 2:
    print(f"{num1} and {num2} are twin primes")
else:
    print(f"{num1} and {num2} are not twin primes")

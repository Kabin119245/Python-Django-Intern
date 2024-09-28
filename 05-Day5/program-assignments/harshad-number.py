num = int(input("Enter any integer number: "))
sum_of_digits = 0
temp = num

while temp > 0:
    sum_of_digits += temp % 10  
    temp = temp // 10  

if num % sum_of_digits == 0:
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is not a Harshad number")

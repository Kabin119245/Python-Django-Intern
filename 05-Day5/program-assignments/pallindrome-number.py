num = int(input("Enter any integer number"))
original = num
sum = 0
i = 0

while num != 0:
    r = num % 10
    sum = sum * 10 + r
    num = num//10
    i = i + 1

if(sum == original):
    print(f"{original} is a pallindrome number")
else:
    print(f"{original} is not a pallindrome number")
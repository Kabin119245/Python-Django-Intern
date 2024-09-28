number=int(input('Enter any integer number: '))
list=[]
for i in range(1,(number)):
    if(number%i==0):
        list.append(i)
sum=0
for x in list:
    sum=sum+x
if(number==sum):
    print(f'{number} is a Perfect number')
else:
    print(f'{number} is not a perfect number')
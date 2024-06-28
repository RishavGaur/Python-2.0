'''Write a python script to check whether a given number is Prime or not.'''

num= int(input("Enter a Number:"))
count=0
i=1

# First Method

'''while i<=num:
    if num%i==0:
        count+=1
    i+=1'''


# Second Method

for x in range(1,num+1):
    if num%x==0:
        count+=1
    x+=1

if count==2:
    print(f'{num} is a Prime Number')
else:
    print(f'{num} is not a Prime Number')
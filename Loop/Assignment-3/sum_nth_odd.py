''' Write a python script to calculate sum of first N Odd Natural Numbers. Value of N is taken from user '''

nth= int(input("Enter nth Number:"))

sum=0
i=1
while i<=nth:
    if i%2!=0:
        sum+=i
    i+=1
print("Sum of nth Odd Natural Numbers=",sum)
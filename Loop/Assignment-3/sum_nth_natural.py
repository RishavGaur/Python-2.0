''' Write a python script to calculate sum of first N Natural Numbers. Value of N is taken from user '''

nth= int(input("Enter nth Number:"))
sum=0
i=1
while i<=nth:
    sum+=i
    i+=1
print("Sum of nth Natural Numbers=",sum)
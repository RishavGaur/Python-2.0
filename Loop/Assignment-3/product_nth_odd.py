''' Write a python script to calculate Product of first N Odd Natural Numbers. Value of N is taken from user '''

nth= int(input("Enter nth Odd Number:"))

product=1
i=1
while i<=nth:
    if i%2!=0:
        product*=i
    i+=1

print("Product of nth Odd Numbers=",product)
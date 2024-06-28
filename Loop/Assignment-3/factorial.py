''' Write a python script to calculate Factorial of a Number. Value of N is taken from user '''

num= int(input("Enter a Number:"))
n=num
fact=1


# First Method
'''while num>0:
    fact= fact*num
    num-=1
'''


# Second Method
i=1
while i<=num:
    fact*=i
    i+=1


print("Factorial of %d is %d"%(n,fact))
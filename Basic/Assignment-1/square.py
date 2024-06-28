# Write a python script to calculate Square of a given number(Number is taken from user)

from math import pow
# Taking a Number to find their Square
num= int(input("Enter a Number:"))
print("Square of %d is %d"%(num,pow(num,2)))
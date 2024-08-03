'''
Two numbers are input through the keyboard into two 
locations C and D. Write a program to interchange the 
contents of C and D. 
'''
a= eval(input("Enter the first number: "))
b= eval(input("Enter the second number: "))
c=a
a=b
b=c
print("Numbers after swapped:")
print("first=",a)
print("second=",b)
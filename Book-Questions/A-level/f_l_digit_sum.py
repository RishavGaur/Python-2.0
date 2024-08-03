'''
If a four-digit number is input through the keyboard, write a 
program to obtain the sum of the first and last digit of this 
number.
'''
num= int(input("Enter a five-digit number: "))

l=num%10
num=num/10000
f=num%10
add= int(l)+int(f)
print("Sum of first and last digit=",add)
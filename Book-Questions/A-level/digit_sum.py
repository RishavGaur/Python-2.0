'''
If a five-digit number is input through the keyboard, write a 
program to calculate the sum of its digits. 
'''
num= int(input("Enter a five-digit number: "))

a=num%10
num=num/10
b=num%10
num=num/10
c=num%10
num=num/10
d=num%10
num=num/10
e=num%10
add= int(a)+int(b)+int(c)+int(d)+int(e)
print("Sum of digit=",add)

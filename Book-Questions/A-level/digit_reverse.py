'''
If a five-digit number is input through the keyboard, write a 
program to reverse the number.
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

reverse= int(a)*10000+int(b)*1000+int(c)*100+int(d)*10+int(e)
print("Reverse of the Number=",reverse)
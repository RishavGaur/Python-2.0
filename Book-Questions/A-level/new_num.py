'''
If a five-digit number is input through the keyboard, write a 
program to print a new number by adding one to each of its 
digits. For example if the number that is input is 12391 then 
the output should be displayed as 23402.
'''
num=int(input("Enter a five-digit number: "))
a= num%10
num=num/10
b=num%10
num=num/10
c=num%10
num=num/10
d=num%10
num=num/10
e=num%10

new=(int(e)+1)*10000+(int(d)+1)*1000+(int(c)+1)*100+(int(b)+1)*10+int(a)+1
print("New Number by adding one to each of its digits=",new)
''' Write a python script to print first N Natural Numbers in reverse order. Value of N is taken 
from user '''

nth= int(input("Enter nth Number:"))
i=nth
while i>0:
    print(i,end=', ')
    i-=1
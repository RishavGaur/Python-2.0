''' Write a python script to print first N Natural Numbers. Value of N is taken from user '''

nth= int(input("Enter the nth Number: "))
i=1
while i<=nth:
    print(i,end=', ')
    i+=1
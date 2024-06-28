''' Write a python script to print first 10 Odd Natural Numbers '''

print("First 10 Odd Natural Numbers are:",end='')

count=0
num=1
while count<10:
    if num%2!=0:
        print(num)
        count+=1
    num+=1
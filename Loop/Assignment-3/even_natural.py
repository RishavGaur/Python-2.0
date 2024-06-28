''' Write a python script to print first 10 Even Natural Numbers '''

print("First 10 Even Natural Numbers are:",end='')
count=0
num=1
while count<10:
    if num%2==0:
        print(num,end=',')
        count+=1
    num+=1
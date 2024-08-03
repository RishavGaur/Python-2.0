'''
Any year is input through the keyboard. Write a program to 
determine whether the year is a leap year or not.
'''
year=int(input("Enter an Year: "))
if year%4==0 and year%100!=0 or year%400==0 and year%100==0:
    print("It's a Leap Year")
else:
    print("It's a non-leap year")
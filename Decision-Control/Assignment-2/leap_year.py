# Write a python script to check if a year is leap year or not.

year= int(input("Enter an Year:"))

if year%4==0 and year%100!=0:
    print("Given Year is Leap Year.")
elif year%400==0 and year%100==0:
    print("Given year is Leap Year.")
else:
    print("Given year is not Leap Year")
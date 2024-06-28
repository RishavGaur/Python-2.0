# Write a python script to take month value in numeric format and display number of days in it.

month= int(input("Enter the Month(in number):"))

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("This Month has 31 days")
elif month==4 or month==6 or month==9 or month==11:
    print("This Month has 30 days")
elif month==2:
    year= int(input("Enter the Year:"))
    if year%4==0 and year%100!=0 or year%400==0 and year%100==0:
        print("This Month has 29 days.")
    else:
        print("This Month has 28 days.")
else:
    print("Please Enter the Correct Month")
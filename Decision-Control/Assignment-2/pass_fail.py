''' Write a python script to accept marks of five subjects from user(assuming maximum marks is 100).
Display Student's Result as PASS or FAIL. If the student is PASS then also display his percentage and
division.'''

print("Enter Five Subjects Marks:")
phy,chem,math,eng,hind= int(input()),int(input()),int(input()),int(input()),int(input())

total= phy+chem+math+eng+hind
perc= total/5

if perc>60 and perc<100:
    print("Pass","\nPercentage=",perc,"\nDivision= 1st")
elif perc>50 and perc<60:
    print("Pass","\nPercentage=",perc,"\nDivision= 2nd")
elif perc>30 and perc<50:
    print("Pass","\nPercentage=",perc,"\nDivision= 3rd")
else:
    print("Failed\nBetter Luck Next Time :)")
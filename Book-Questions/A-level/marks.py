'''
If the marks obtained by a student in five different subjects 
are input through the keyboard, find out the aggregate marks 
and percentage marks obtained by the student. Assume that 
the maximum marks that can be obtained by a student in each 
subject is 100. 
'''

phy= eval(input("Enter the marks in Physics: "))
che= eval(input("Enter the marks in Chemistry: "))
mth= eval(input("Enter the marks in Maths: "))
eng= eval(input("Enter the marks in English: "))
hin= eval(input("Enter the marks in Hindi: "))
total= phy+che+mth+eng+hin
per= total/500*100
print("Total marks Obtained by the Student=",total)
print("Percentage=",per)
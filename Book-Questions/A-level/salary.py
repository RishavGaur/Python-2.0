'''
Ramesh’s basic salary is input through the keyboard. His 
dearness allowance is 40% of basic salary, and house rent 
allowance is 20% of basic salary. Write a program to calculate 
his gross salary. 
'''

salary= eval(input("Enter the basic salary of Ramesh: "))
da= 4/10*salary
hra= 2/10*salary
g_salary= salary+da+hra
print("Dearness Allowance=",da)
print("House Rent Allowance=",hra)
print("Gross Salary=",g_salary)
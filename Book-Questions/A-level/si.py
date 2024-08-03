'''
Python Script to find Simple Interest.
'''
p=eval(input("Enter the Principle Amount: "))
r=eval(input("Enter the Rate of Interest(in %): "))
t=eval(input("Enter Time Period(in year): "))
si= (p*r*t)/100
print("Simple Interest=",si)
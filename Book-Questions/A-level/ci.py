'''
Python Script to find Compound Interest.
'''
from math import pow

p=eval(input("Enter the Principle Amount: "))
r=eval(input("Enter the Rate of Interest(in %): "))
t=eval(input("Enter Time Period(in year): "))

ci= p*pow(1+r/100,t)-p
print("Compound Interest=",ci)
'''
The length & breadth of a rectangle and radius of a circle are 
input through the keyboard. Write a program to calculate the 
area & perimeter of the rectangle, and the area & 
circumference of the circle.
'''
from math import pi,pow
length,breadth= eval(input("Enter the Length of a Rectangle: ")),eval(input("Enter the Breadth of a Rectangle: "))
radius= eval(input("Enter the Radius of the Circle: "))
area_rec= length*breadth
peri_rec= 2*(length+breadth)
area_cir= pi*pow(radius,2)
cirf_cir= 2*pi*radius
print("Area of Rectangle=",area_rec)
print("Perimeter of Rectangle=",peri_rec)
print("Area of Circle=",area_cir)
print("Circumference of Circle=",cirf_cir)
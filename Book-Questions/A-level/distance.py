'''
The distance between two cities (in km.) is input through the 
keyboard. Write a program to convert and print this distance 
in meters, feet, inches and centimeters.
'''
distance= eval(input("Enter the distance b/w two cities(in Kilometer): "))
meter= distance*1000
feet= meter*3.28
cm= meter*100
inch= feet*12
print("Distance b/w two cities in:")
print("Meter=",meter,"\nFeet=",feet,"\nCentimeter=",cm,"\nInches=",inch)
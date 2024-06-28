# Write a python script to find greatest among three numbers.

num1= int(input("Enter the first Number:"))
num2= int(input("Enter the second Number:"))
num3= int(input("Enter the third Number:"))

if num1>num2 and num1>num3:
    print("First number as %d is greatest among all"%num1)
elif num2>num1 and num2>num3:
    print("Second number as %d is greatest among all"%num2)
else:
    print("Third number as %d is greatest among all"%num3)
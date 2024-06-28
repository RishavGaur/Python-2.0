'''Write a python script to accept one complex number from user and display the greater number between
  real part and imaginary part.'''

comp_num= complex(input("Enter a Complex Number(e.g. 3+4j):"))

real_part= comp_num.real
imag_part= comp_num.imag

if real_part>imag_part:
    print("The greater part is",real_part)
elif imag_part>real_part:
    print("The greater part is",imag_part)
else:
    print("Both are Equal")
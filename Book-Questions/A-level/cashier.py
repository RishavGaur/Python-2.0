'''
A cashier has currency notes of denominations 10, 50 and 
100. If the amount to be withdrawn is input through the 
keyboard in hundreds, find the total number of currency notes 
of each denomination the cashier will have to give to the 
withdrawer.
'''
amount= int(input("Enter the returnable amount: "))

hund= amount/100
amount=amount%100
fift=amount/50
amount=amount%50
ten=amount/10
amount=amount%10
five=amount/5
amount=amount%5
one=amount/1

print("Returnable Amount in Cash are:")
print("Hundred Rupees Note=",int(hund))
print("Fifty Rupees Note=",int(fift))
print("Ten Rupees Note=",int(ten))
print("Five Rupees Note=",int(five))
print("One Rupees Coin=",int(one))
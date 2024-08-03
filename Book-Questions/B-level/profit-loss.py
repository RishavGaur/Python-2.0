'''
If cost price and selling price of an item is input through the 
keyboard, write a program to determine whether the seller has 
made profit or incurred loss. Also determine how much profit 
he made or loss he incurred.
'''
cp=eval(input("Enter the Cost Price of an item: "))
sp=eval(input("Enter the Selling Price of an item: "))
if sp>cp:
    profit= sp-cp
    print("Seller has made Profit of",profit,"Rs")
else:
    loss= cp-sp
    print("Seller has made Loss of",loss,"Rs")
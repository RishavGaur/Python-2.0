'''
If the total selling price of 15 items and the total profit earned 
on them is input through the keyboard, write a program to 
find the cost price of one item.
'''
selling_amount= eval(input("Enter the Selling Price of 15 items: "))
profit= eval(input("Enter the Profit earned amount: "))
non_profit= selling_amount-profit
item_price= non_profit/15
print("Cost Price of one item=",item_price)
cost_price=float(input("enter the cost price:"))
sell_price=float(input("enter the selling price:"))
if sell_price>cost_price:
    print("profit:  ",sell_price-cost_price)
elif sell_price==cost_price:
    print("no profit and loss")    
else:
    print("loss:",cost_price-sell_price)    
actual_price=int(input("enter the actual price"))
selling_price=int(input("enter the selling price"))

if actual_price<selling_price:
    print("profit",selling_price - actual_price)

else:
    print("no profit")
items_price = [10, 20, 80, 450, 360, 550, 30, 90, 100,1000,75]
for i in items_price:
    if i >= 500:
        print("You cannot buy this item")
        continue
    print(i)
print("Shopping Completed")
    
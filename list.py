# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print("i have", len(shoplist), "items to purchase.")
print('These items are:', end=' ')
for items in shoplist:
    print(items,end=" ")

print("\nI have also rice to buy")
shoplist.append("rice")

print("My shopping list",shoplist)

shoplist.sort()
print("The sorted item list are",shoplist)

oldList = shoplist[0]
del shoplist[0]

print("The item i bought first is",oldList)
print("Now my shopping list is",shoplist)
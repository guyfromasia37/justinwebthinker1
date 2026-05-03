print("Hello from lesson 14")
import random
for i in range(1,6):
    num=random.randint(1,6)
    print(num)
fruitos=["apple","banana","cherry","durian"]
pricetos=["2 dolla","3 dolla","5 dolla","10 dolla"]
for i in range(len(fruitos)):
    print(fruitos[i]+"cost $"+pricetos[i])
items=["apple","milk","bread","egg","chocolate"]
stock=[15,0,8,25,3]
print("inventory stock check")
for i in range(len(items)):
    if stock[i]==0:
        status="out of stock"
    elif stock[i]<10:
        status="low stock"
    else:
        status="well stocked"
    print("item:"+items[i]0+"qty:"+str(stock[i])+"status"+status)
sl=["eraser","notebook","pencil","pens"]
print("shopping list")
counter=input("how many more item i buy?")

for i in range(len(counter)):
    item=input("what item i buy")\
    sl.append(item)



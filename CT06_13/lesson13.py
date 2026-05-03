
groceries=["apple","bread","carrots","dates","eggs","flour","grapes","honey"  ]
print(groceries)
groceries[7]="herbs"
print(groceries)
for i in groceries:
    print(i)
groceries.append("milk")
groceries.insert(3,"curry")
print(groceries)
groceries.append("ice")
groceries.insert(1,"banana")
print(groceries)
groceries.pop(3)
print(groceries)




grocery=[]
while True:
    user=input("what itemssssssssssssssssssss")
    grocery.append(user)
    if user=="end":
        break
for items in grocery:
    print("i have bought"+items)
print(grocery)

catalouge=[]
while True:
    user=input("enter items")
    if user =="end":
        break
    else:
        catalouge.append(user)


for i in catalouge:
    print(i)




items=["water","taters","gun","oil","milk","carrot","beff"]
user=input("item?")
if user==items:
    print("we sell that")
else:
    print("GETOUT")


toppings=["mushroom","olives","pepperoni","mystery meat","pineapple","apple","not so cooked pig","beff","bird that cant fly","CHESSSSSSSSSSSSSSSSS"]
rt=[]
for i in range(len(toppings)):
    print(str(i+1)+"."+toppings[i])

while True:
    user=input("TOPPINGSSS?????????")
    if user !="end":
        rt.append(user)
    else:
        break
        

print("Hello from lesson 12")



num=int(input("numpls"))
if (num%3==0 and num%5==0):
    print("it is divisable by 3 and 5")
else:
    print("nahbruv")


visitors=int(input("visit?"))
maxvisitor=int(input("max allowed"))
while visitors <maxvisitor:
    visitors+=1
    print("visitors")

rv=0
while True:
    rv+=1
    print("rv")
    if rv == 30:
        break

order=""
while True:
    orders=input("welcome to the white market what ur order")
    if orders=="end":
        break
    order=order+orders
print("order")




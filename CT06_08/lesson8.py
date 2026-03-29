print("if the code is your power,what are you without it?")
import time





cdn = int(input("what is the meaning of donuts?"))
for i in range(cdn):
    print(i)
    time.sleep(1)
print("118 BRACE FOR IMPACT!nuke sounds, entire world blows up")



import random
#print(random.random())#gives random number between 0 and less than 1 data type is a float
#print(random.radint())#gives u a random integer data type is integer
for count in range(20):
    lucky_num=print(random.randint(0,40))
    print(str(count + 1)+ "." + str(lucky_num))
print(random.randint(1,50))
guess = input("enter your guess")
if guess == "random_num":
    print("correct")
else:
    print("wrong")



num1 = random.randint(1,50)
num2 = random.randint(1,50)
user = input("what is"+str(num1)+"+"+str(num2)+"?")
realans=num1+num2
if int(user) == realans:
    print(True)
else:
    print(False)

randomnum = random.randint(1,50)
guessone = input("start")
guesstwo = input("end")
if randomnum >=guessone:
    if randomnum <= guesstwo:
            print(True)
else:
     print(False)
    


num=2
if num%2==0:
    print("its a even!")
else:
    print("its a odd!")


num1=(input("gimme a number"))
num2=(input("gimme another"))
if int(num1)%int(num2) ==0:
    print(num1+"is a multiple of" +num2)
else:
    print(num1+"is not a multiple of" +num2)


print("Hello from lesson 10")
num=input("gimme a num")

if int(num)>0 :
    print("the num is positive")
else:
    print("the num is negative")


age=int(input("what age bruv"))
if age <13:
    print("xiao hai zi")
else:
    if(age>=13 & age<19):
        print("xavier")
    else:
        if age <60:
            print("lao uncle/lao anty")

temp=int(input("what temp?"))
if temp>6767:
    print("commit self-murder before you get evaporated by a atomic-hydrogen bomb")
elif temp>30:
    print("swimming")
elif temp >25 & temp<30:
    print("basketball")
elif temp >20 & temp <24:
    print("cycle")
else:
    print("read a book")

score = int(input("enter score"))
if score >90 & score <100:
    print("A")
elif score>80 & score<89:
    print("B")
elif score>70 & score<79:
    print("C")
elif score>60 & score<69:
    print("D")
elif score>50 & score<59:
    print("E")
elif score>0 & score<49:
    print("F")
else:
    if score<-1:
        print("get a job at mcdonalds failure")


mone=int(input("how much money xavier"))
if mone>9999999999:
    print("xavier can buy the usa but its economy would be gone in a hour")
elif mone>150 and mone<200:
    print("he can buy 10 children from the white market")
elif mone>100 and mone<149:
    print("he can buy palu escuba")
elif mone>50 and mone<99:
    print("he can buy a chinese airpline with bluetooth on it")
elif mone>20 and mone<49:
    print("he could buy a potato PC")
elif mone>0 and mone<19:
    print("he could buy a year in india")
else: 
    if mone<-1:
        print("he can buy the poop of the 10 kids he bought from the white market")
print("Hello from lesson 7")


sum = 0
for i in range(5):
    num = input("marks")
    sum+= int(num)
avg = sum/5
print(avg)





num = int(input("what number???"))

for i in range(1,12):
    print(str(num)+"x"+str(i)+"="+str(num*i))

for count in range(12):
    count += 1
    print(str(num)+"x"+str(count)+"="+str(num*count))


num2=int(input("gimme number brochaco"))
for i in range(num2):
    print(str(i+1)*(i+1))

sum2 = 0
numstu = int(input("how many kids:]"))
for i in range(numstu):
    score = input("score?")
    sum2+= int(score)
avg2 = sum2/numstu
print(avg2)
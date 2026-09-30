while True:
    name = input("enter the name:")
    total = 0
    while True:
        print("Enter the amount and Quantity")
        amount = float(input("enter the amount:"))
        quantity = float(input("Enter the Quantity of the item:"))
        total += amount*quantity
        repeat = input("Do you want to repeat the item(yes/no):")
        if repeat == "no" or "No":
            break
    print("---------------------------")
    print("Name:",name)
    print("Total:",total)   
    print("-----------------------------")
    repeat = input("do you want to continue(yes/no):")
    if repeat == "no" or repeat == "No":
        break 
a = "I am siddamma"
print("the length of string is:",len(a))
print("how many times the o alphabet occures:",a.count("m"))
print("convert the string into upper case:",a.upper())
print("convert the string into title:",a.title())
print('the index of the alphabet "s" is:',a.index("s"))


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()



for i in range(1,6):
    for j in range(6,i,-1):
        print(j,end=" ")
    print()    



for i in range (1,6):
    for j in range (1,i+1):
        print(i,end = " ") 
    print()  


for i in range (1,6):
    for j in range (5,i,-1):
        print(" ",end = " ") 
    for k in range (i):
        print("*",end = " ")         
    print()

for i in range (1,6):
    for j in range (i,0,-1):
        print(j,end = " ") 
    print()  


for i in range (1,11):
    for j in range (1,i+1):
        print(i*j,end = " ")  
    print()      
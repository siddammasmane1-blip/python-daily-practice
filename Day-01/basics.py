for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print() 

for i in range(1,6):
    for k in range(5-i):
        print(" ",end=" ")
        
    for j in range(1,i+1):
        print("*",end=" ")
    print()    

num = int(input("enter the largest number:"))
if num > 9:
    print("number is larger:")
else:
    print("number is smaller:")

    
num = int(input("enter the number:"))
largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num //10
print("the largest number is :",largest) 


num = int(input("enter the number:"))
for i in range(2,51):
    if i > 1:
        print("the prime numbers are:",i)

num = 7
for i in range (2,num):
     if num % i == 0:
         print(" not prime number")
         break
else:
          print("prime number")
#divisible by 8 and 12
for i in range(1,101):
     if i % 8 == 0 and i % 12 == 0:
          print(i)
    

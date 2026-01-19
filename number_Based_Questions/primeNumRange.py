import math

num = int(input("Enter a Number :"))

def checkPrime(num):
    if num <= 1:
        return False
    
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True

for i in range(0,num):
    if checkPrime(i) is True:
        print(i,end=" ")

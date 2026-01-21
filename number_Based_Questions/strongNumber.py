num = int(input("Enter a Number :"))

def strongNum(num):
    num2 = num
    finalNum = 0
    while num != 0:
        rem = num % 10
        finalNum = finalNum + factorial(rem)
        num = num // 10
        
    if finalNum == num2:
        return(True)
    return False


def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    
    return fact

print(strongNum(num))
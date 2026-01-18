num = int(input("Enter a Number :"))

def countFunction(num):
    count = 0
    while num != 0:
        count = count + 1
        num = num // 10
    return count

def checkArmstrong(num):
    num2 = num
    finalNum = 0
    count = countFunction(num)
    while num != 0:
        rem = num % 10
        finalNum = finalNum + rem**count
        num = num // 10
    
    if finalNum == num2:
        return True
    return False
    
if checkArmstrong(num) is True:
    print("Number is Armstrong !")
else:
    print("Number is not Armstrong !")
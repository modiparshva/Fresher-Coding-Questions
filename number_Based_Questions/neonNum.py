num = int(input("Enter a Number :"))

def checkNeon(num):
    square = num * num
    temp = square
    finalNum = 0
    
    while temp != 0:
        rem = temp % 10
        finalNum = finalNum + rem
        temp = temp // 10
        
    if finalNum == num:
        return True
    return False

print(checkNeon(num))
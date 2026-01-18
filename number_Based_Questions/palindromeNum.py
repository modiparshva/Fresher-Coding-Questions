num = int(input("Enter Number :"))

def checkPalindrome(value):
    num = value
    finalNum = 0
    num2 = num
    while num != 0:
        rem = num % 10
        finalNum = finalNum * 10 + rem
        num = num // 10
        
    if finalNum == num2:
        return True
    else :
        return False           
    
if checkPalindrome(num) is True:
    print("Palindrome !")
else :
    print("Not a Palindrome !")
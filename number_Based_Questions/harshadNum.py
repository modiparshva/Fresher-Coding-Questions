# A Harshad Number (also called a Niven Number) is a number that is divisible by the sum of its digits.

def checkHarshad(num):
    temp = num
    sum = 0
    while temp != 0:
        rem = temp % 10
        sum = sum + rem
        temp = temp // 10
        
    if num % sum == 0:
        return True
    return False

print(checkHarshad(18))
print(checkHarshad(19))
print(checkHarshad(21))
        
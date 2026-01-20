num = int(input("Enter a Number :"))

def sumOfDigits(num):
    sum = 0
    while num != 0:
        rem = num % 10
        sum = sum + rem
        num = num // 10
    return sum

print(sumOfDigits(num))
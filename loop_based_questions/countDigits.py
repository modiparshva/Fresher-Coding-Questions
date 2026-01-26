num = int(input("Enter a Number :"))

def countingDigit(num):
    count = 0
    while num != 0:
        count = count + 1
        num = num // 10
    return count

print(countingDigit(num))
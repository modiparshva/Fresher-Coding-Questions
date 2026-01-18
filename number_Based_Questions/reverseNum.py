num = int(input("Enter a Number :"))

def countFunction(num):
    count = 0
    while num != 0:
        count = count + 1
        num = num // 10
    return count

def reverse(num):
    num2 = 0
    count = countFunction(num)
    while num != 0:
        rem = num % 10
        num2 = num2 * 10 + rem
        num = num // 10
    
    count2 = countFunction(num2)
    if count == count2:
        return num2
    else:
        num3 = str(num2)
        num3 = "0" * (count-count2) + num3
        return num3

print(reverse(num))
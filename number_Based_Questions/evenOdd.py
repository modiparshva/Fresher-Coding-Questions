num = int(input("Enter a Number :"))

def checkEvenOdd(num):
    if num % 2 == 0:
        return True
    return False


if checkEvenOdd(num) is True:
    print("Even Number !")
else:
    print("Odd Number !")
    

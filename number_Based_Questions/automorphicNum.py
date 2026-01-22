# Automorphic Number is a Number whose square ends with the same digits as the number itself.

# Examples -> 25 -> 625, 76 -> 5776, 5 -> 25, etc.

def checkAutomorphic(num):
    square = num * num
    digits = len(str(num))
    
    if (square % (10 ** digits)) == num:
        return True
    return False

print(checkAutomorphic(76))
print(checkAutomorphic(25))
print(checkAutomorphic(7))

# How it Works : 

# num = 76
# square = 5776
# digits = 2
# 10^2 = 100

# 5776 % 100 = 76

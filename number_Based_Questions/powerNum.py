# Power of Number

num = int(input("Enter Base Num :"))
exp = int(input("Enter Exponent Num :"))

result = 1
for i in range(exp):
    result = result * num
    
print(result)
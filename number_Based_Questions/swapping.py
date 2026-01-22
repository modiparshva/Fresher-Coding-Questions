num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))


# Swapping Without Temp Variable
# Method 1
# num1,num2 = num2,num1 

# Method 2
# num1 = num1 + num2
# num2 = num1 - num2
# num1 = num1 - num2

# Swapping with Temp Variable

temp = num1
num1 = num2
num2 = temp

print("Num1 :",num1)
print("Num2 :",num2)
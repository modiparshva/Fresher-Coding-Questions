value = input("Enter String :")
def checkPalindrome(value):
    i = 0
    j = len(value) - 1
    while i <= j:
        if value[i] != value[j]:
            return False
        i = i+1
        j = j-1
    return True

print(checkPalindrome(value)) 
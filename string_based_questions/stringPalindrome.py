str1 = "racecar"
def checkPalindrome(str1):
    i = 0
    j = len(str1)-1
    while i <= j:
        if (str1[i] != str1[j]):
            return False
        i = i + 1
        j = j - 1
    return True

print(checkPalindrome(str1))
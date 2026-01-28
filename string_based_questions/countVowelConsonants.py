str1 = "ParShva"

def countVowelConst(str1):
    vowels = "aeiouAEIOU"
    vowel = 0
    consonants = 0
    
    for ch in str1:
        if ch.isalpha(): # Ignore non-alphabet characters
            if ch in vowels:
                vowel += 1
            else:
                consonants += 1
    
    return vowel,consonants

v,c = countVowelConst(str1)
print(f"Total Number of Vowels are {v} and Total Numbers of Consonants are {c}")

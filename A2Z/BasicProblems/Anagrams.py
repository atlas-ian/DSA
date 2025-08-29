def anagram(str1, str2):
    

    if sorted(str1) == sorted(str2):
        return True
    return False


str1 = "silent"
str2 = "listen"
print(anagram(str1,str2))
print(sorted(str1))
print(sorted(str2))
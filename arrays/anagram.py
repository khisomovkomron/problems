def is_anagram(str1, str2):
    
    
    if len(str1) != len(str2):
        return False
    
    str1 = list(str1)
    str2 = list(str2)
    
    str1 = sorted(str1)
    str2 = sorted(str2)
    
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
        
    return True


if __name__ == "__main__":
    str1 = 'fluster'
    str2 = 'restful'
    
    print(is_anagram(str1, str2))
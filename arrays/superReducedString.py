
def superReducedString(s):
    
    i  = 0
    
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            s = s[i+2:] if i == 0 else s[:i] + s[i+2:]
            i = 0
            
        else:
            i += 1
            
    return print("Empty String") if len(s)==0 else print(s)


word = 'aaabccddd'
print(word[3:])
superReducedString(word)


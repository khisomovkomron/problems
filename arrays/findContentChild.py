def findContentChildren(g: list[int], s: list[int]) -> int:

    count = 0
    i = 0
    j = 0
    
    while i < min(len(g), len(s)):
        if g[i] <= s[j]:
            count += 1
            i += 1
        j += 1

    return count


print(findContentChildren(g=[1, 2, 3, 4], s=[1, 2, 3, 4, 5, 6, 7]))

def thirdMax(nums: list[int]) -> int:
    """Given an integer array nums, return the third distinct maximum number in this array.
    If the third maximum does not exist, return the maximum number."""
    
    s = list(set(nums))
    s.sort(reverse=True)
    
    if len(s)<3:
        return max(s)
    else:
        return s[2]

print(thirdMax(nums=[-1, 2, 3]))

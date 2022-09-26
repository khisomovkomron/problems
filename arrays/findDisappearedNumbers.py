def findDisappearedNumbers(nums: list[int]) -> list[int]:
    """Given an array nums of n integers where nums[i] is in the range [1, n],
    return an array of all the integers in the range [1, n] that do not appear in nums."""

    s1 = [x for x in range(1, len(nums) + 1)]
    for num in nums:
        s1[num - 1] = 0
    s1 = [i for i in s1 if i != 0]
    return s1
    
    
print(findDisappearedNumbers(nums=[4,3,2,7,8,2,3,1]))
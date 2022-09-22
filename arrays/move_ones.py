def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(0)
            nums.remove(0)
    
print(moveZeroes(nums=[0,1,0,3,12]))

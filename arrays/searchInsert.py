def searchInsert(nums: list[int], target: int) -> int:
    for i in range(len(nums)-1):
        if nums[i] == target:
            return i
        else:
            nums.append(target)
            new_nums = sorted(nums)
            for y in range(len(new_nums) - 1):
                if new_nums[y] == target:
                    return y
            

        
nums = [1,3,5,6]
print(searchInsert(nums, target=7))
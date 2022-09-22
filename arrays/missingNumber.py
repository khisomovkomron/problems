def missingNumber(nums: list[int]) -> int:

    # sorted_nums = list(sorted(nums))
    #
    # i = 1
    # while i < len(sorted_nums):
    #     if sorted_nums[i-1]+1 == sorted_nums[i]:
    #         i += 1
    #     else:
    #         return sorted_nums[i-1]+1
    #
    # return len(sorted_nums)

    # for i in range(len(nums) + 1):
    #     if i in nums:
    #         pass
    #     else:
    #         return i
    
    completed = list(range(len(nums)+1))
    return sum(completed) - sum(nums)

print(missingNumber(nums=[0, 1]))

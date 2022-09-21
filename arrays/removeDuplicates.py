
def removeDuplicates(nums: list[int]) -> int:
    
    nums[:] = sorted(set(nums))
    return nums


nums = [0,0,1,1,1,2,2,3,3,4,5,5,5,7,7,7,7]
# print(f"nums {nums}")
print(f"nums = {removeDuplicates(nums)}")
class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
        
    
obj = NumArray(nums=[-2, 0, 3, -5, 2, -1])
print(obj.sumRange(left=0, right=5))
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    
    d = {}
    
    for i in range(len(nums)):
        num = nums[i]
        
        if num in d:
            if abs(d[num] - i) <= k:
                return True
        d[num] = i
    return False
            



print(containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=2))
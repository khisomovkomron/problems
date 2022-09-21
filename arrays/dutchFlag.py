



def dutch_flat(nums, pivot=1):
    
    i = 0
    j = 0
    k = len(nums) - 1
    
    while j <= k:
        
        if nums[j] < pivot:
            swap(nums, i, j)
            i = i + 1
            j = j + 1
        elif nums[j] > pivot:
            swap(nums, j, k)
            k = k - 1
        else:
            j = j + 1
    return nums
    
    
def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]

n = [0, 2, 1, 1, 0, 2, 1]
print(dutch_flat(n, pivot=1))
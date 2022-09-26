def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must be unique and you may return the result in any order."""
    # list = []
    # i = 0
    # j = 0
    # while i < len(nums1):
    #     while j < len(nums2):
    #         if nums1[i] == nums2[j]:
    #             list.append(nums1[i])
    #             i += 1
    #             j += 1
    #         else:
    #             j += 1
    #     i += 1
    #     j = 0
    #
    # return list
    #

    nums1, nums2 = set(nums1), set(nums2)
    inter_list = []
    
    for i in nums1:
        
        if i in nums2:
            inter_list.append(i)
            
    return set(inter_list)

print(intersection(nums1=[1], nums2=[1]))
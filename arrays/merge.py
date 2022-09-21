def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # i= 0
    # j= 0
    # nums1 = nums1[:m]
    # nums2 = nums2[:n]
    # while i < m and j < n:
    #     i += 1
    #     j += 1
    #     if nums1[i] > nums2[j]:
    #         nums1.insert(i, nums2[j])
    #
    #     elif nums1[i] < nums2[j]:
    #         nums1.insert(i+1, nums2[j])
    #
    #     else:
    #         nums1.insert(i, nums2[j])
    #
    # nums1 = sorted(nums1)
    # print(nums1)

    # solution 2
    del nums1[m:]
    nums1.extend(nums2)
    nums1.sort()
    print(nums1)
            
merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)
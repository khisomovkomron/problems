def summaryRanges(nums: list[int]) -> list[str]:

    i = 0
    result = []
    
    while i < len(nums):
        j = i + 1
        
        while j < len(nums):
            # check if number+1 == number, if number is one less than next
            if nums[j-1]+1 == nums[j]:
                # if yes, pass one index to the right
                j += 1
            else:
                break
            
            # if number is alone, added to list, [1]
        if j-i == 1:
            result.append(str(nums[j-1]))
        # if number is more than 1, [1,2,3]
        else:
            result.append(str(nums[i]) + ">" + str(nums[j-1]))
        # change i to the last j, start i from last j
        i = j
    
    return result


print(summaryRanges(nums=[0, 1, 2, 4, 5, 7]))

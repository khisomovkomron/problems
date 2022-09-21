def plusOne(digits: list[int]) -> list[int]:
    remainder = 1
    
    for i in reversed(range(len(digits))):
        sum = digits[i] + remainder
        digits[i] = sum % 10
        remainder = sum // 10
        
    if remainder == 1:
        digits.insert(0, 1)
    return digits

    # remains = 1
    # for i in reversed(range(len(digits))):
    #     sum = digits[i] + remains
    #     digits[i] = sum % 10
    #     remains = sum // 10
    #
    # if remains == 1:
    #     digits.insert(0, 1)
    # return digits
    

print(plusOne(digits=[9,9,9,4,5,6,5,6,5,6,5,6,5,6,9]))
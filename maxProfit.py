def maxProfit(prices: list[int]):
    
    for i in range(len(prices)):
        list = []
        for j in range(i+1, len(prices)):
            print(prices[j], prices[i])
            if prices[j] >= prices[i]:
            
                list.append((prices[j], i))
            else:
                list.append((prices[j], i))
                # list.pop()
        
   
    return list


print(maxProfit(prices=[7,1,5,3,6,4]))
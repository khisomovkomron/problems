"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def maxProfit(prices: list[int]) -> int:
    # [7,1,5,3,6,4]
    # for i in range(len(prices)+1):
    #
    #     min_index = 0
    #
    #     if prices[i] < prices[i+1]:
    #         min_index = prices[i]
    
    i = 0
    j = 1
    max_index = 0
    while j < len(prices):
        if prices[i] < prices[j]:
            max_index = max(max_index, prices[j] - prices[i])
        else:
            i = j
        j += 1
   
    return max_index

print(maxProfit(prices=[7,1,5,3,6,4]))


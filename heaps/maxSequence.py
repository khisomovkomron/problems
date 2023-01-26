import heapq
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        tuple_heap = []

        for i, val in enumerate(nums):
            if len(tuple_heap) == k:
                heapq.heappushpop(tuple_heap, (val,i))
            else:
                heapq.heappush(tuple_heap, (val, i))
        print(tuple_heap)
        tuple_heap.sort(key=lambda x: [1])
        print(tuple_heap)
        ans = []
        for i in tuple_heap:
            ans.append(i[0])
        print(ans)
        return ans


if __name__ == "__main__":

    s  =  Solution()

    s.maxSubsequence(nums = [2,1,3,3], k = 2)
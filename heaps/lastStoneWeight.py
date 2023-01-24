from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, s in enumerate(stones):
            stones[i] = -s

        heapq.heapify(stones)
        s1 = -heapq.heappop(stones)
        while stones:
            s1 = -heapq.heappop(stones)

            if not stones:
                return s1
            s2 = - heapq.heappop(stones)
            if s1 > s2:
                heapq.heappush(stones, s2-s1)
        return 0


if __name__ == "__main__":


    stone = Solution()
    result = stone.lastStoneWeight([2,7,4,1,8,1])
    assert result == 1
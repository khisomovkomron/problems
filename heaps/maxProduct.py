from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ls = sorted([-i for i in nums])

        return (ls[0]+1) * (ls[1]+1)


if __name__ == "__main__":

    s = Solution()
    print(s.maxProduct(nums=[3,4,5,2]))


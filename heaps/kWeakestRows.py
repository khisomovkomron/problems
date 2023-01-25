from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        S = [[sum(m), i] for i, m in enumerate(mat)]
        print(S)
        R = sorted(S)
        print(R)
        print([r[1] for r in R[:k]])

if __name__ == "__main__":

    s = Solution()

    s.kWeakestRows(mat=[[1,1,0,0,0],
                         [1,1,1,1,0],
                         [1,0,0,0,0],
                         [1,1,0,0,0],
                         [1,1,1,1,1]], k=3)
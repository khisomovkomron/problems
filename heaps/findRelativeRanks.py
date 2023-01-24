from copy import deepcopy
from typing import List
import heapq
class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[int]:
        scoreCopy = []
        for i in score:
            scoreCopy.append(i)
        heapq.heapify(scoreCopy)
        print(score)
        index = len(score)
        place = {}
        while len(scoreCopy) > 0:
            item = heapq.heappop(scoreCopy)
            place[item] = index
            index -= 1

        print(place)
        res = []
        for i in range(len(score)):
            match place[score[i]]:
                case 1:
                    res.append('Gold Medal')
                case 2:
                    res.append('Silver Medal')
                case 3:
                    res.append("Bronze Medal")
                case _:
                    res.append(str(place[score[i]]))
        print(res)
        return res

    def fix_down(self, score: List[int]) -> List[int]:
        ls = deepcopy(score)
        index = 0
        left = 2 * index + 1
        right = 2 * index + 2
        largest_index = index

        if left < len(ls) and ls[index] < ls[left]:
            largest_index = left
            print(ls)

        if right < len(ls) and ls[index] < ls[right]:
            largest_index = right
            print(ls)

        if index != largest_index:
            ls[index], ls[largest_index] = ls[largest_index], ls[index]
            self.fix_down(largest_index)
            print(ls)

        return ls

if __name__ == "__main__":

    findRR = Solution()
    result = findRR.findRelativeRanks(score=[5,4,3,2,1])
    assert result == ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

    result2 = findRR.findRelativeRanks(score=[10,3,8,9,4])

    assert result2 == ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
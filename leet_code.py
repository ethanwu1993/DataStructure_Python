

from typing import List


class Solution:

    def __init__(self) -> None:
        pass

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        new_nums = list(set(groupSizes))

        output = []
        for i in new_nums:
            index_li = []
            for j in groupSizes:
                print(i, j)
                if i == j:
                    index_li.append(groupSizes.index(j))
            print(index_li)




s = Solution()
a = s.groupThePeople([3,3,3,3,3,1,3])

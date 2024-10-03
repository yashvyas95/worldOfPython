from typing import List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        container = {}
        for i in range(len(arr)):
            if k-arr[i] in container:
                return True
            else:
                container[arr[i]]=i
        return False


Solution = Solution()
Solution.canArrange([1,2,3,4,5,6],10)

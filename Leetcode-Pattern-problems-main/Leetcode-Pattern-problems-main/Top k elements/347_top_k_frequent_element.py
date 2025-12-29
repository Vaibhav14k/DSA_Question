import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n<k:
            return nums
        freq = Counter(nums)
        ans = []
        for i in freq.items():
            heapq.heappush(ans,(i[1],i[0]))
            if len(ans)>k:
                heapq.heappop(ans)
        ans = [num for frequency,num in ans]
        return ans
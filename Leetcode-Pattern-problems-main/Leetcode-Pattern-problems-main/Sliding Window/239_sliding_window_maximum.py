import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, heap = [], []

        for i in range(k):
            heapq.heappush(heap, [-nums[i], i])

        curr_max = -heap[0][0]
        res.append(curr_max)

        for i in range(k, len(nums)):
            heapq.heappush(heap, [-nums[i], i])
            curr_max = heap[0]

            while curr_max[1] <= i-k:
                heapq.heappop(heap)
                curr_max = heap[0]
            
            res.append(-curr_max[0])

        return res


obj = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(obj.maxSlidingWindow(nums, k))  
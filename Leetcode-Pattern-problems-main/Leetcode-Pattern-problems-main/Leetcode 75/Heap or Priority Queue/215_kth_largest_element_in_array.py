import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        arr = nums[:k]
        heapq.heapify(arr)
        print(arr)
        for i in range(k, len(nums)):
            if nums[i] > arr[0]:
                heapq.heappop(arr)  
                heapq.heappush(arr, nums[i])
        print(arr)
        return arr[0]


obj = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(obj.findKthLargest(nums,k))
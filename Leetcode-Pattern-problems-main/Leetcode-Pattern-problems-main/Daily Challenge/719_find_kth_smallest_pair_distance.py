import heapq
class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        def countPairs(mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if countPairs(mid) < k:
                low = mid + 1
            else:
                high = mid
        
        return low

        '''arr = []
        n = len(nums)
        nums.sort()
        print(nums)
        for first in range(n):
            for second in range(first + 1, n):
                arr.append(abs(nums[first] - nums[second]))
        arr.sort()
        return arr[k-1]'''  


obj = Solution()
nums = [1,3,1,5,9]
k = 2
print(obj.smallestDistancePair(nums, k))  
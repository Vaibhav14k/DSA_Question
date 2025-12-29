class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        prefix_map = {0,1}
        count = 0

        for num in nums:
            # Update prefix sum 
            prefix_sum += num
            # Help to find if we found subset
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]
            # To update frequency prefix sum
            if prefix_sum in prefix_map:
                prefix_map[prefix_sum] += 1
            else:
                prefix_map[prefix_sum] = 1
        return count

obj = Solution()
nums = [1,1,1]
k = 2
nums = [1,2,3]
k = 3
nums = [-1,-1,1]
k = 0
print(obj.subarraySum(nums, k))  
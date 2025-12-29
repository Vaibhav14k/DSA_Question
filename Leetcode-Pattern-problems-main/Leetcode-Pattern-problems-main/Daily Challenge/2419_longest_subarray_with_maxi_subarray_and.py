class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maxx = max(nums)
        max_length = 0
        curr_length = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == maxx:
                curr_length += 1
            else:
                curr_length = 0
            max_length = max(curr_length,max_length)
        return max_length

obj = Solution()
nums = [1,2,3,3,2,2]
# Output: 2
print(obj.longestSubarray(nums))
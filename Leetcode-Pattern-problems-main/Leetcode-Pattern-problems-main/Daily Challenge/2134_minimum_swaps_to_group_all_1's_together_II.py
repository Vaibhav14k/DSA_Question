class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        total = nums.count(1)
        nums += nums[:total-1]
        current_swap = sum(nums[:total])
        total_mini_swaps = total - current_swap
        for i in range(1, n):
            current_swap += nums[i + total - 1] - nums[i-1]
            total_mini_swaps = min(total_mini_swaps,total - current_swap)
        return total_mini_swaps


obj = Solution()
nums = [0,1,1,1,0,0,1,1,0]
# nums = [0,1,0,1,1,0,0]
# nums = [1,1,0,0,1]
print(obj.minSwaps(nums)) 
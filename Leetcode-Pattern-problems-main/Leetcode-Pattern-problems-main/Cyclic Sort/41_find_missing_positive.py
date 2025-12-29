class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = set(nums)
        for i in range(1,len(nums)+2):
            if (i not in nums):
                return i


obj = Solution()
nums = [1,2,0]
# nums = [3,4,-1,1]
nums =[7,8,9,11,12]
nums = [2,1]
print(obj.firstMissingPositive(nums))

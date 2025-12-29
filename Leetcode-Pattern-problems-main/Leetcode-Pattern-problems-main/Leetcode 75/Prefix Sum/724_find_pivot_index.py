class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right = sum(nums)
        left = 0

        for i in range(len(nums)):
            left = sum(nums[0:i])
            right -= nums[i]
            if right == left:
                return i
        return -1

obj = Solution()
nums = [4,1,4]
nums = [1,7,3,6,5,6]
nums = [1,2,3]
print(obj.pivotIndex(nums))
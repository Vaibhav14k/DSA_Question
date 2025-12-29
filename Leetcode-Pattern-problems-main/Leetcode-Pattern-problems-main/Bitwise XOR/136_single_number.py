class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res =0
        for i in nums:
            res = res ^ i
        return res

nums = [4,1,2,1,2]
obj = Solution()
print(obj.singleNumber(nums))
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        for i in nums:
            sub = []
            for j in res:
                sub.append(j+[i])
            res.extend(sub)
        print(res)

obj = Solution()
nums = [1,2,3]
nums = [0]
print(obj.subsets(nums))
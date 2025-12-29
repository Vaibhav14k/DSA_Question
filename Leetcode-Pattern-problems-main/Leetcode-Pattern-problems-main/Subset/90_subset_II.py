class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        nums.sort()
        for i in nums:
            sub = []
            print("res",res)
            for j in res:
                if j+[i] not in res:
                    sub.append(j+[i])
            print("sub",sub)
            res.extend(sub)
        return res

obj = Solution()
nums = [1,2,2]
nums = [4,4,4,1,4]
print(obj.subsetsWithDup(nums))
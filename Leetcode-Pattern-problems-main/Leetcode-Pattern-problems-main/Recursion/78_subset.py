class Solution:
    def solve(self,nums,ans,op,index):
        if index >= len(nums):
            # copy is added so that next recursive calls don't affect the op
            ans.append(op.copy())
            return
        # exclude case
        self.solve(nums,ans,op,index+1)
        # include case 
        op.append(nums[index])
        self.solve(nums,ans,op,index+1)
        op.pop()

    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        op = []
        index =  0
        self.solve(nums,ans,op,index)
        return ans


obj = Solution()
print(obj.subsets([1, 2, 3]))
class Solution:
    def solve(self,nums,ans,index):
        print("ans-->",ans)
        print("nums-->",nums)
        if index == len(nums):
            ans.append(nums[:])
            return
        for i in range(index,len(nums)):
            nums[index],nums[i] = nums[i],nums[index]
            self.solve(nums,ans,index+1)
            nums[index],nums[i] = nums[i],nums[index]
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        index = 0
        self.solve(nums,ans,index)
        return ans 

obj = Solution()
print(obj.permute([1, 2, 3]))
print(obj.permute([1, 2, 3,4,5]))
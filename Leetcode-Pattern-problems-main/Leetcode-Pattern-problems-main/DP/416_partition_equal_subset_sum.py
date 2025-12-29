class Solution:
    ''' RECURSION
    def solve(self,nums,index,target):
        if index == len(nums):
            return 0
        if target<0:
            return 0
        if target == 0:
            return 1
        inc = self.solve(nums,index+1,target-nums[index])
        exc = self.solve(nums,index+1,target)
        return inc or exc
    def canPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2 == 1:
            return False
        return self.solve(nums,0,sum(nums)//2)
    '''
    '''RECURSION + MEMOIZATION
    def solve(self,nums,index,target,dp):
        if index == len(nums):
            return 0
        if target<0:
            return 0
        if target == 0:
            return 1
        if dp[index][target] != -1:
            return dp[index][target]
        inc = self.solve(nums,index+1,target-nums[index],dp)
        exc = self.solve(nums,index+1,target,dp)
        dp[index][target] = inc or exc
        return dp[index][target]
    def canPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        target = sum(nums)//2
        if sum(nums) % 2 == 1:
            return False
        dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1 )]
        return self.solve(nums,0,target,dp)
    '''
    def solve(self,nums):
        n = len(nums)
        target = sum(nums)//2
        curr = [0] * (target + 1)
        next = [0] * (target + 1)
        curr[0] = next[0] = 1
        for index in range(n-1,-1,-1):
            for target in range(target+1):
                inc = 0
                if target >= nums[index]:
                    inc = next[target-nums[index]]
                exc = next[target]
                curr[target] = inc or exc
            next = curr[:]
        return next[target]
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        return self.solve(nums)

obj = Solution()
nums = [1,5,11,5]
print(obj.canPartition(nums))
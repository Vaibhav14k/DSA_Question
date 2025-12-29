class Solution:
    ''' RECURSION + TABULATION
    def solve(self,nums,n,dp):
        if n<0:
            return 0
        if n==0:
            return nums[0]
        if dp[n]!=-1:
            return dp[n]
        inc = self.solve(nums,n-2,dp) + nums[n]
        exc = self.solve(nums,n-1,dp) 
        dp[n] = max(inc,exc)
        return dp[n]
    '''
    ''' TABULATION
    def solve(self,nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1,n):
            inc = dp[i-2] + nums[i]
            exc = dp[i-1] + 0
            dp[i] = max(inc,exc)
        return dp[n-1]
    '''
    def solve(self,nums):
        n = len(nums)
        dp = [0] * n
        prev1 = 0
        prev2 = nums[0]
        for i in range(1,n):
            inc = prev1 + nums[i]
            exc = prev2 + 0
            ans = max(inc,exc)
            prev1 = prev2
            prev2 = ans
        return prev2

    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        return self.solve(nums)

obj = Solution()
nums = [1,2,3,1]
print(obj.rob(nums))
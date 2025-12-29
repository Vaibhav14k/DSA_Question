from bisect import bisect_left
class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,nums,curidx,previdx,dp):
        if curidx==len(nums):
            return 0
        if dp[curidx][previdx+1]!=-1:
            return dp[curidx][previdx+1]
        inc = 0
        if previdx == -1 or nums[curidx]>nums[previdx]:
            inc = 1 + self.solve(nums,curidx+1,curidx,dp)
        exc = self.solve(nums,curidx+1,previdx,dp)
        dp[curidx][previdx+1] = max(inc,exc)
        return dp[curidx][previdx+1]
    '''
    ''' TABULAR METHOD
    def solve(self,nums):
        n = len(nums)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        inc = 0
        for curr in range(n-1,-1,-1):
            for prev in range(curr-1,-2,-1):
                if prev == -1 or nums[curr]>nums[prev]:
                    # Here at start curr is n-1 
                    inc = 1 + dp[curr+1][curr+1]
                exc = dp[curr+1][prev+1]
                dp[curr][prev+1] = max(inc,exc)
        # return dp[0][-1+1]
        return dp[0][0]
    '''
    '''
    def solve(self,nums):
        n = len(nums)
        curr_row = [0] * (n+1)
        next_row = [0] * (n+1)
        for curr in range(n-1,-1,-1):
            for prev in range(curr-1,-2,-1):
                inc = 0     
                if prev == -1 or nums[curr]>nums[prev]:
                    inc = 1 + next_row[curr+1]
                exc = next_row[prev+1]
                curr_row[prev+1] = max(inc,exc)
            next_row = curr_row[:]
        return next_row[0]
    '''
    def solve(self,nums):
        n = len(nums)
        if n == 0:
            return 0
        
        ans = []
        ans.append(nums[0])
        for i in range(1,n):
            if nums[i]>ans[-1]:
                ans.append(nums[i])
            else:
                idx = bisect_left(ans,nums[i])
                ans[idx] = nums[i]
        print(ans)
        return len(ans)

    def lengthOfLIS(self, nums: list[int]) -> int:
        # dp = [[-1 for _ in range(len(nums)+1)] for _ in range(len(nums))]
        # return self.solve(nums,0,-1,dp)
        return self.solve(nums)

obj = Solution()
nums  = [5,8,3,7,9,1]
print(obj.lengthOfLIS(nums))
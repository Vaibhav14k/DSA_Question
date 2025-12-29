class Solution:
    ''' TOP-DOWN
    def solve(self,cost,n,dp):
        if n == 0:
            dp[n]=0
            return cost[0]
        if n == 1:
            dp[n]=1
            return cost[1]
        if dp[n] != -1:
            return dp[n]
        dp[n] = min(self.solve(cost,n-1,dp),self.solve(cost,n-2,dp))+cost[n]
        return dp[n]
    '''
    '''BOTTOM-UP
    def solve(self,cost,n,dp):
        n = len(cost)
            dp = [-1] *(n+1)
            dp[0] = cost[0]
            dp[1] = cost[1]
            for i in range(2,n+1):
                dp[i] = min(dp[i-1],dp[i-2])+cost[i]
            return min(dp[n-1],dp[n-2])
    '''
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # BOTTOM-UP (space optimized)
        n = len(cost)
        prev1 = cost[0]
        prev2 = cost[1]
        for i in range(2,n):
            temp = cost[i] + min(prev1,prev2)
            prev1 = prev2
            prev2 = temp
        return min(prev1,prev2)

obj = Solution()
cost = [10,15,20]
print(obj.minCostClimbingStairs(cost))
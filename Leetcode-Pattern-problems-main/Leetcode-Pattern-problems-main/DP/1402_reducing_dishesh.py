class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,score, index, time,dp):
        if index == len(score):
            return 0
        if dp[index][time] != -1:
            return dp[index][time]
        inc = score[index] * (time) + self.solve(score,index + 1, time + 1,dp)
        exc = self.solve(score,index + 1, time,dp)
        dp[index][time] = max(inc,exc)
        return dp[index][time]
    '''
    ''' TABULATION METHOD
    def solve(self,score, index, time):
        n = len(score)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for index in range(n-1,-1,-1):
            for time in  range(n-1,-1,-1):
                inc = score[index] * (time + 1) + dp[index + 1] [time + 1]
                exc = dp[index + 1] [time]
                dp[index][time] = max(inc,exc)
        return dp[index][time]
    '''
    def solve(self,score, index, time):
        n = len(score)
        curr = [0 for _ in range(n+1)]
        next = [0 for _ in range(n+1)]
        for index in range(n-1,-1,-1):
            for time in  range(n-1,-1,-1):
                inc = score[index] * (time + 1) + next[time + 1]
                exc = next [time]
                curr[time] = max(inc,exc)
            next = curr[:]
        return curr[time]
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        # n = len(satisfaction)
        # dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        satisfaction.sort()
        return self.solve(satisfaction,0,0)

obj = Solution()
print(obj.maxSatisfaction([-1,-8,0,5,-9]))
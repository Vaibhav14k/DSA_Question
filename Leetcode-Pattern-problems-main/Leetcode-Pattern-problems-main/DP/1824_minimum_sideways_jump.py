class Solution:
    '''RECURSION + MEMOIZATION
        def solve(self,obs, currlane, currpos,dp):
            if currpos == len(obs)-1:
                return 0
            if dp[currlane][currpos] != -1 :
                return dp[currlane][currpos]
            if obs[currpos + 1] != currlane:
                return self.solve(obs,currlane,currpos+1,dp)
            else:
                ans = float("inf")
                for i in range(1,4):
                    if currlane != i and obs[currpos] != i :
                        ans = min(ans, 1 + self.solve(obs,i,currpos+1,dp))
                dp[currlane][currpos] = ans 
                return dp[currlane][currpos]
    '''
    def solve(self,obs,currlane,currpos):
        n = len(obs) -1 
        dp = [[float('inf') for _ in range(len(obstacles)) ] for _ in range(4)]
        # Base case 
        dp[0][n] = 0
        dp[1][n] = 0
        dp[2][n] = 0
        dp[3][n] = 0

        for pos in range(n-1,-1,-1):
            for lane in range(1,4):
                if obs[pos + 1] != lane:
                    dp[lane][pos] =  dp[lane][pos + 1]
                else:
                    ans = float("inf")
                    for i in range(1,4):
                        if lane != i and obs[pos] != i :
                            ans = min(ans, 1 + dp[i][pos + 1])
                    dp[lane][pos] = ans 
        return  min(dp[2][0], min (1 +dp[1][0], 1 + dp[3][0] ))

    def minSideJumps(self, obstacles: list[int]) -> int:
        return self.solve(obstacles,2,0)

obj = Solution()
obstacles = [0,1,2,3,0]
print(obj.minSideJumps(obstacles))
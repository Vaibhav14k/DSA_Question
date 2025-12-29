class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,start,end,memo):
        if start >= end:
            print("Base case")
            return 0
        # if (start,end) in memo:
        #     print("Memoization")
        #     return memo[(start,end)]
        if memo[start][end] != -1:
            print("Memoization")
            return memo[start][end]
        ans = float('inf')
        for i in range(start,end+1):
            ans = min(ans,i+ max(self.solve(start,i-1,memo),self.solve(i+1,end,memo)))
        memo[start][end] = ans
        return memo[start][end] 
    def getMoneyAmount(self, n: int) -> int:
        # memo = {}
        memo = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.solve(1,n,memo)
    '''
    def solve(self,n):
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
        for start in range(n,0,-1):
            for end in range(start,n+1):
                if start==end:
                    continue
                ans = float("inf")
                for k in range(start,end+1):
                    ans = min(ans,k+ max(dp[start][k-1],dp[k+1][end]))
                dp[start][end] = ans
        return dp[1][n] 

    def getMoneyAmount(self, n: int) -> int:
        return self.solve(n)

obj = Solution()
n = 10
print(obj.getMoneyAmount(n)) 
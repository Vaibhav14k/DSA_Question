class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,n,dp):
        if n==0:
            return 0
        if dp[n] != -1:
            return dp[n]
        ans = n
        i =1
        while i*i<=n:
            ans = min(1+self.solve(n-i**2,dp),ans)
            i+=1
        dp[n] = ans
        return dp[n]
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.solve(n,dp)
    '''
    def solve(self,n):
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for j in range(1,n+1):
            i =1
            while i*i<=n:
                dp[j] = min(1+dp[j-i**2],dp[j])
                i+=1
        return dp[n]
    def numSquares(self, n: int) -> int:
        return self.solve(n)

obj = Solution()
print(obj.numSquares(12))
''' RECURSION + MEMOIZATION
def solve(n,k,dp):
        if n==1:
            return k
        if n==2:
            return k*k
        if dp[n] != -1:
            return dp[n]
        mod = 10 **9 + 7
        dp[n]= ((solve(n-2,k,dp)* (k-1))
                + (solve(n-1,k,dp) * (k-1)
                ))%mod
        return dp[n]
'''
''' TABULATION
def solve(n,k):
        dp = [-1]* (n+1)
        if n==1:
            return k
        if n==2:
            return k*k
        dp[1]=k
        dp[2] = k*k
        for i in range(3,n+1):
            same = dp[i-2] * (k-1)
            diff = dp[i-1] * (k-1)
            dp[i] = (same + diff) % (10**9 + 7)
        return dp[n]
'''
def solve(n,k):
        if n==1:
            return k
        if n==2:
            return k*k
        prev1 = k
        prev2 = k*k
        for i in range(3,n+1):
            same = prev1 * (k-1)
            diff = prev2 * (k-1)
            ans = (same + diff) % (10**9 + 7)
            prev1 = prev2
            prev2 = ans
        return prev2
def paintFence(n:int,k:int)->int:
    # dp = [-1]*(n+1)
    # return solve(n,k,dp)
    return solve(n,k)


n=2
k = 3
print(paintFence(n,k))
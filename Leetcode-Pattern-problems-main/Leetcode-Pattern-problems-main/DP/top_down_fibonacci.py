def fib(n,dp):
    if n==0 or n==1:
        return n
    if n in dp:
        return dp[n]
    else:
        dp[n] = fib(n-1,dp) + fib(n-2,dp)
        return dp[n]


n = 6
dp = [0]*(n+1)
print(fib(n,dp))
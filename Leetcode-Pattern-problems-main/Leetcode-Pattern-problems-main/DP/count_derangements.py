def countDerangements(n,dp):
    ''' RECURSION + MEMOIZATION
    if n==1:
        return 0
    if n==2:
        return 1
    if dp[n] != -1:
        return dp[n]
    mod = 10**9 + 7
    dp[n] = (((n - 1) % mod) * ((countDerangements(n - 2,dp) % mod) + (countDerangements(n - 1,dp) % mod)) % mod)
    return dp[n]
    '''
    if n==1:
        return 0
    if n==2:
        return 1
    mod = 10**9 + 7
    prev1 = 0
    prev2 = 1
    for i in range(3,n+1):  
        first = prev1 % mod
        second = prev2 % mod
        add = (first + second) %mod
        ans = (i-1  * add)%mod
        dp[i] = ans
        prev1 = prev2
        prev2 = ans
    return prev2

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [-1] * (n + 1)
    print(countDerangements(n, dp))
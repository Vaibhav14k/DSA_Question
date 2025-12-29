def fib(n):
    if n<=1:
        return n
    prev1 = 0
    prev2 = 1
    for i in range(2,n+1):
        temp = prev1 + prev2
        prev1 = prev2
        prev2 = temp
    return prev2
    '''
    Less optimized
    dp = [-1]*(n+1)
    dp[1] = 1
    dp[0] = 0
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
    '''


print(fib(6))
''' RECURSION + MEMOIZATION
def solve(n,x,y,z,dp):
    if n==0:
        return 0
    if n<0:
        return float('-inf')
    if dp[n] != -1:
        return dp[n]
    a = solve(n-x,x,y,z,dp)
    b = solve(n-y,x,y,z,dp)
    c = solve(n-z,x,y,z,dp)
    dp[n] = max(a,max(b,c)) +1
    return dp[n]
'''
''' TABULATION
def solve(n,x,y,z):
    dp = [float('-inf')]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        if i>=x:
            dp[i] = max(dp[i],dp[i-x]+1)
        if i>=y:
            dp[i] = max(dp[i],dp[i-y]+1)
        if i>=z:
            dp[i] = max(dp[i],dp[i-z]+1)
    return dp[n]
'''
def solve(n,x,y,z):
    dp = [float('-inf')]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        if i>=x:
            dp[i] = max(dp[i],dp[i-x]+1)
        if i>=y:
            dp[i] = max(dp[i],dp[i-y]+1)
        if i>=z:
            dp[i] = max(dp[i],dp[i-z]+1)
    if dp[n] <0:
        return 0
    else:
        return 
def cutSegments(n, x, y, z):
    ans = solve(n,x,y,z)
    return ans

print(cutSegments(7,5,2,2))
class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,capacity, wt,value,index,dp):
        if index == 0:
            if wt[0]<=capacity:
                return val[0]
            else:
                return 0
        if dp[index][capacity] != -1:
            return dp[index][capacity]
        inc = 0
        if wt[index]<=capacity:
            inc = self.solve(capacity-wt[index], wt,value,index-1,dp) + value[index]
        exc = self.solve(capacity, wt,value,index-1,dp) + 0
        dp[index][capacity] = max(inc,exc)
        return dp[index][capacity]
    '''

    def solve(self,capacity, wt,value,n):
        dp = [[-1 for _ in range(capacity + 1)] for _ in range(n)]
        # Base case 
        for w in range(capacity + 1):
            if wt[0] <= w:
                dp[0][w] = value[0]
            else:
                dp[0][w] = 0

        for index in range(1,n):
            for w in range(0,capacity+1):
                inc = 0
                if wt[index]<=capacity:
                    inc = dp[index-1][w-wt[index]] + value[index]
                exc = dp[index-1][w]
                dp[index][w] = max(inc,exc)
        return dp[n-1][capacity]


    def knapSack(self,W, wt, val, n):
        # dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
        # return self.solve(W,wt,val,n-1,dp)
        return self.solve(W,wt,val,n)

n=3
capacity=4
wt=[4,5,1]
val=[1,2,3]
obj = Solution()
print(obj.knapSack(capacity,wt,val,n))
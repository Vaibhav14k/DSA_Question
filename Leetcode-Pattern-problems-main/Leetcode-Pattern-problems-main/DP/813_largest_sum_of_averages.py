class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,grid,n,k,memo):
        if n== 0 and k==0 :
            return 0
        if n== 0 or k==0 :
            return -float("inf")
        if (n,k) in memo:
            return memo[(n,k)]
        maxx = -float("inf")
        for i in range(n):
            maxx = max(maxx,self.solve(grid,i,k-1,memo) + grid[i][n-1])
        memo[(n,k)] = maxx
        return memo[(n,k)]
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        n = len(nums)
        grid = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n-1,i-1,-1):
                grid[i][j] = sum(nums[i:j+1])/(j-i+1)
        # print(grid)
        n = len(grid)
        memo = {}
        return self.solve(grid,n,k,memo)
    '''
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        n = len(nums)
        grid = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n-1,i-1,-1):
                grid[i][j] = sum(nums[i:j+1])/(j-i+1)
        # print(grid)
        n = len(grid)
        # # dp[l][m] will store the maximum sum of m subsets from first l elements
        dp = [[-float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for l in range(1, n + 1):
            for m in range(1, k + 1):
                for p in range(0, l):
                    dp[l][m] = max(dp[l][m], dp[p][m-1] + grid[p][l-1])
        return dp[n][k]

nums = [9,1,2,3,9]
k = 3
obj = Solution()
print(obj.largestSumOfAverages(nums,k))

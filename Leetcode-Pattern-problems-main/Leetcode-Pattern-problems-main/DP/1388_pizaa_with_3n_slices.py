class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,index,n,slices,end_index,dp):
        if n==0 or index >end_index:
            return 0
        if dp[index][n] != -1:
            return dp[index][n]
        incl = slices[index] + self.solve(index+2,n-1,slices,end_index,dp)
        excl = 0 + self.solve(index+1,n,slices,end_index,dp)
        dp[index][n] = max(incl,excl)
        return dp[index][n]
    def maxSizeSlices(self, slices: list[int]) -> int:
        n = len(slices)
        dp1 = [[-1 for _ in range(n)] for _ in range(n)]
        inc = self.solve(0,n//3,slices,n-2,dp1)
        dp2 = [[-1 for _ in range(n)] for _ in range(n)]
        exc = self.solve(1,n//3,slices,n-1,dp2)
        return max(inc,exc)
    '''
    ''' BOTTOM UP APPROACH
    def solve(self,slices):
        k = len(slices)
        dp1 = [[0 for _ in range(k+2)] for _ in range(k+2)]
        dp2 = [[0 for _ in range(k+2)] for _ in range(k+2)]
        # REMOVING LAST ELEMENT
        for index in range(k-2,-1,-1):
            for n in range(1,k//3 +1):
                incl = slices[index] + dp1[index+2][n-1]
                excl = 0 + dp1[index+1][n]
                dp1[index][n] = max(incl,excl)
        inc = dp1[0][k//3]
        # REMOVING FIRST ELEMENT
        for index in range(k-1,0,-1):
            for n in range(1,k//3+1):
                incl = slices[index] + dp2[index+2][n-1]
                excl = 0 + dp2[index+1][n]
                dp2[index][n] = max(incl,excl)
        exc = dp2[1][k//3]
        return max(inc,exc)
    def maxSizeSlices(self, slices: list[int]) -> int:
        n = len(slices)
        return self.solve(slices)
    '''
    def solve(self,slices):
        k = len(slices)
        curr1 =[0] * (k+2)
        prev1 =[0] * (k+2)
        next1 =[0] * (k+2)
        # REMOVING LAST ELEMENT
        for index in range(k-2,-1,-1):
            for n in range(1,k//3 + 1):
                incl = slices[index] + next1[n-1]
                excl = 0 + curr1[n]
                prev1[n] = max(incl,excl)
            next1 = curr1[:]
            curr1 = prev1[:]
        inc = curr1[k//3]

        curr2 =[0] * (k+2)
        prev2 =[0] * (k+2)
        next2 =[0] * (k+2)
        # REMOVING FIRST ELEMENT
        for index in range(k-1,0,-1):
            for n in range(1,k//3 +1):
                incl = slices[index] + next2[n-1]
                excl = 0 + curr2[n]
                prev2[n] = max(incl,excl)
            next2 = curr2[:]
            curr2 = prev2[:]
        exc = curr2[k//3]
        return max(inc,exc)
    def maxSizeSlices(self, slices: list[int]) -> int:
        return self.solve(slices)


obj = Solution()
slices = [1,2,3,4,5,6]
print(obj.maxSizeSlices(slices))
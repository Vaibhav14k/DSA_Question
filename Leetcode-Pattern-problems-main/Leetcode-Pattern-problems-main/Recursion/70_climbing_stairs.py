class Solution:
    def climbStairs(self, n: int) -> int:
        # In leetcode it's given with time limit of DP
        if n<0:
            return 0
        if n==0:
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)
    
obj = Solution()
print(obj.climbStairs(3)) 
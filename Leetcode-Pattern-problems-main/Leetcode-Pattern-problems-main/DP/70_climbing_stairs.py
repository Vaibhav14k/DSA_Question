class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=1:
            return n
        prev1 = 1
        prev2 = 1
        for i in range(2,n+1):
            temp = prev1 + prev2
            prev1 = prev2
            prev2 = temp
        return prev2

obj = Solution()
print(obj.climbStairs(3)) 
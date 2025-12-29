class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        return (n%2 == 0) and self.isPowerOfTwo(n//2)

obj = Solution()
print(obj.isPowerOfTwo(4))
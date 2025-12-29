class Solution:
    def grayCode(self, n: int) -> list[int]:
        res = [0]
        for i in range(n):
            res += [x+(1<<i) for x in reversed(res)]
        return res

n = 2
obj = Solution()
print(obj.grayCode(n))
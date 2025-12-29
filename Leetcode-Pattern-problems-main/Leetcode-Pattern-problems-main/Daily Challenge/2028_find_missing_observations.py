import random
class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        m = len(rolls)
        total = (n + m) * mean
        remaining = total - sum(rolls)
        if remaining < n or remaining > n * 6:
            return []
        sol = [1] * n
        remaining -= n
        while remaining > 0:
            i = random.randint(0,n-1)
            if sol[i] < 6:
                sol[i] += 1
                remaining -= 1
        return sol

obj = Solution()
rolls = [3,2,4,3]
mean = 4, n = 2
# Output: [6,6]
obj.missingRolls(rolls,mean,n)
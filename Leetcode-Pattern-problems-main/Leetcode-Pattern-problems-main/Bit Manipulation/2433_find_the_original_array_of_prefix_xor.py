class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        sol = [pref[0]]
        n = len(pref)
        res = pref[0]
        for i in range(1,n):
            sol.append(pref[i] ^ res)
            res ^= sol[i]
        return sol

obj = Solution()
pref = [5,2,0,3,1]
# Output: [5,7,2,3,2]
print(obj.findArray(pref))
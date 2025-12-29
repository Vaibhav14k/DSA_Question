class Solution:
    def removeStars(self, s: str) -> str:
        sol = []
        for i in s:
            if i!="*":
                sol.append(i)
            else:
                sol.pop()
        print(sol)
        return "".join(sol)

obj = Solution()
s = "erase*****"
s = "leet**cod*e"
print(obj.removeStars(s))

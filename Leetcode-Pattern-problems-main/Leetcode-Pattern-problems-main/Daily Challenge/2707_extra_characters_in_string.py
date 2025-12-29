class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        words = set(dictionary)
        memo = {}
        def solve(i):
            if i == len(s):
                return 0
            if s[i:] in memo:
                return memo[s[i:]]
            res = 1 + solve(i+1) # skipp karo
            for j in range(i,len(s)):
                if s[i:j+1] in words:
                    res = min(res,solve(j+1))
            memo[s[i:]] = res
            return memo[s[i:]]
        return solve(0)

s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
obj = Solution()
print(obj.minExtraChar(s,dictionary))
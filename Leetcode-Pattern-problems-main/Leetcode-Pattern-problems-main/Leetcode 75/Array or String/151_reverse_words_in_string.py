class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        return " ".join(s)
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        sol = ""
        res = s.split(" ")
        res.reverse()
        for i in range(len(res)):
            if res[i] != "":
                sol += res[i] +" "
        return sol.rstrip()
'''
obj = Solution()
s = "the sky is blue"
s = "  hello world  "
s = "example   good a"
print(obj.reverseWords(s))
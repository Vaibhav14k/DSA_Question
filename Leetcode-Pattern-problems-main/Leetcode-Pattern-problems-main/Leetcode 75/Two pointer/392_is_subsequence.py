class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first = second = 0
        while first<len(s) and second<len(t):
            if s[first] == t[second]:
                first +=1
            else:
                second +=1
        if  first== len(s):
            return True
        else:
            return False

obj = Solution()
s = "axc"
t = "ahbgdc"
print(obj.isSubsequence(s,t))
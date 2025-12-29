class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str2+str1 != str1+str2:
            return ""
        from math import gcd 
        return str1[:gcd(len(str1),len(str2))]

obj = Solution()
str1 = "ABCABC"
str2 = "ABC"
str1 = "ABABAB"
str2 = "ABAB"
str1 = "LEET"
str2 = "CODE"
print(obj.gcdOfStrings(str1,str2))
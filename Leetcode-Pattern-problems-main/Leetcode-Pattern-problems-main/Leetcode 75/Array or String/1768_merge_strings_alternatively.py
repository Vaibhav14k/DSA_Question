class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        minn = min(len(word1),len(word2))
        res = ""
        for i in range(minn):
            res +=word1[i]
            res +=word2[i]
        if  minn<n:
            res += word1[minn:]
        if  minn<m:
            res += word2[minn:]
        return res

obj = Solution()
word1 = "abc"
word2 = "pqr"
word1 = "abcd" 
word2 = "pq"
print(obj.mergeAlternately(word1,word2))
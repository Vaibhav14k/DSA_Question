class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,text1,text2,i,j,memo):
        if  i==len(text1) or j==len(text2):
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        if text1[i]==text2[j]:
            memo[i][j] = 1 + self.solve(text1,text2,i+1,j+1,memo)
            return memo[i][j]
        else:
            memo[i][j] = max(self.solve(text1,text2,i+1,j,memo),self.solve(text1,text2,i,j+1,memo))
            return memo[i][j]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return self.solve(text1,text2,0,0,memo)
    '''
    def solve(self,text1,text2):
        curr = [0] * (len(text2)+1)
        next = [0] * (len(text2)+1)
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    ans = 1 + next[j+1]
                else:
                    ans = max(next[j],curr[j+1])
                curr[j] = ans
            next = curr[:]
        return next[0]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.solve(text1,text2)
obj = Solution()
text1 = "abcde"
text2 = "ace" 
print(obj.longestCommonSubsequence(text1, text2))  
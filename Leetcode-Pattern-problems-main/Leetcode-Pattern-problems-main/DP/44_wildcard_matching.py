class Solution:
    ''' RECURSION
    def solve(self,str,pat,i,j):
        # BASE CASE
        if (i<0 and j<0):
            return True

        if (i>=0 and j<0): # abc,bc
            return False

        if (i<0 and j>=0): # abc,***bc OR abc,dabc
            for k in range(j):
                if pat[k] != "*":
                    return False
            return True
        
        # MATCH CASE
        if (str[i] == pat[j] or pat[j] == "?"):
            return self.solve(str,pat,i-1,j-1)
        elif pat[j] == "*":
            return self.solve(str,pat,i-1,j) or self.solve(str,pat,i,j-1)
        else:
            return False
    def isMatch(self, s: str, p: str) -> bool:
        return self.solve(s,p,len(s),len(p))
    '''
    def solve(self,str,pat,i,j,memo):
        # BASE CASE
        if (i<0 and j<0):
            return True

        if (i>=0 and j<0): # abc,bc
            return False

        if (i<0 and j>=0): # abc,***bc OR abc,dabc
            for k in range(j+1):
                if pat[k] != "*":
                    return False
            return True
        if memo[i][j] != -1:
            return memo[i][j]
        # MATCH CASE
        if (str[i] == pat[j] or pat[j] == "?"):
            memo[i][j] = self.solve(str,pat,i-1,j-1,memo)
        elif pat[j] == "*":
            memo[i][j] = self.solve(str,pat,i-1,j,memo) or self.solve(str,pat,i,j-1,memo)
        else:
            memo[i][j] = False
        return memo[i][j]
    def isMatch(self, s: str, p: str) -> bool:
        memo = [[-1 for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        return self.solve(s,p,len(s)-1,len(p)-1,memo)

obj = Solution()
s = "abcde"
p = "a*c?e"
s = "cb"
p = "?a"
s = "abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab"
p = "*aabb***aa**a******aa*"
print(obj.isMatch(s, p)) 
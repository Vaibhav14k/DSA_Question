class Solution:
    def solve(self,curr,res,open,close):
        if open == 0 and close == 0:
            res.append(curr)
            return
        if open > 0:
            self.solve(curr+"(",res,open-1,close)
        if close > open:
            self.solve(curr+")",res,open,close-1)
        return res
    def generateParenthesis(self, n: int) -> list[str]:
        return self.solve("",[],n,n)

n = 3
obj = Solution()
print(obj.generateParenthesis(n))
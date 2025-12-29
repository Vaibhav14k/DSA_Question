class Solution:
    def solve(self,s,ans,op,index):
        print("ans-->",ans,"index-->",index)
        print("op-->",op)
        if index == len(s):
            ans.append(op)
            return
        # exclude
        self.solve(s,ans,op,index+1)
        # include
        op+=s[index]
        self.solve(s,ans,op,index+1)
    def Subsequence(self, s: str) :
        ans = []
        op = ""
        index = 0
        self.solve(s,ans,op,index)


obj = Solution()
s = "abc"
print(obj.Subsequence(s))
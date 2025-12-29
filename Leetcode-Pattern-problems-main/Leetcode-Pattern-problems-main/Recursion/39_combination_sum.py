class Solution:
    def solve(self,candidates,target,i,n,op,res):
        if target==0:
            res.append(op)
            return
        for i in range(n):
            if candidates[i]<=target:
                self.solve(candidates,target-candidates[i],i+1,n,op+[candidates[i]],res)

    def combinationSum(self, candidates:list[int], target: int) -> list[list[int]]:
        res = []
        ans = []
        op = []
        i=0
        n = len(candidates)
        self.solve(candidates,target,i,n,op,res)
        for i in res:
            i.sort()
            if i not in ans:
                ans.append(i)
        # print(ans)
        return ans

obj = Solution()
candidates = [2,3,6,7]
target = 7
print(obj.combinationSum(candidates, target))
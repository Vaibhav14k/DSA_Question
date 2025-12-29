class Solution:
    def solve(self, candidates, target, index, op, res):
        # print("Index-->",index,"Output-->",op,"res-->",res)
        if target == 0:
            res.append(op[:])
            return

        if target < 0 or index >= len(candidates):
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            if target - candidates[i] >= 0:
                # op.append(candidates[i])
                self.solve(candidates, target - candidates[i], i + 1, op + [candidates[i]], res)
                # op.pop()  
        return res

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        return self.solve(candidates, target, 0, [], [])


obj = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(obj.combinationSum2(candidates, target))  
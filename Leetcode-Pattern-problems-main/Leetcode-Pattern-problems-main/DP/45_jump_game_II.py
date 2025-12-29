'''
    def solve(self, nums, i, n,dp):
        if i >= n - 1:
            return 0
        if dp[i] != float("inf"):
            return dp[i]
        min_jumps = float('inf')
        
        for j in range(1, nums[i] + 1):
            if i + j < n:
                jumps = self.solve(nums, i + j, n,dp)
                if jumps != float('inf'):
                    min_jumps = min(min_jumps, jumps + 1)
        dp[i]= min_jumps
        return dp[i]

    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [float('inf')]*(n)
        if n == 0:
            return 0
        return self.solve(nums, 0, n,dp)
'''
class Solution:
    def jump(self, nums: list[int]) -> int:
        def findTargetIndex(target_index, count):
            if target_index == 0:
                return count
            for i in range(len(lt)):
                if lt[i][1] >= target_index:
                    return findTargetIndex(i, count + 1)
        lt = []

        for i in range(len(nums)):
            lt.append((i, i + nums[i]))
        print(lt)
        count = findTargetIndex(len(nums) - 1, 0)
        print(count)
        return count
        


obj = Solution()
nums = [2,3,1,1,4]
print(obj.jump(nums))
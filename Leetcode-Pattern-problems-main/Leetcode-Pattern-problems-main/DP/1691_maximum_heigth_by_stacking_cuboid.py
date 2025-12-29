from bisect import bisect_left
class Solution:
    def check(self,base,newBox):
        if base[0] >= newBox[0] and base[1] >= newBox[1] and base[2] >= newBox[2]:
            return True
        else:
            return False
    
    def solve(self,nums):
        n = len(nums)
        curr_row = [0] * (n+1)
        next_row = [0] * (n+1)
        for curr in range(n-1,-1,-1):
            for prev in range(curr-1,-2,-1):
                inc = 0     
                if prev == -1 or self.check(nums[curr],nums[prev]):
                    inc = nums[curr][2] + next_row[curr+1]
                exc = next_row[prev+1]
                curr_row[prev+1] = max(inc,exc)
            next_row = curr_row[:]
        return next_row[0]

    def maxHeight(self, cuboids: list[list[int]]) -> int:
        for i in cuboids:
            i.sort()
        # cuboids = sorted(cuboids,key=lambda x:(x[0],-x[1]))
        cuboids.sort()
        # print(cuboids)
        return self.solve(cuboids)


obj = Solution()
cuboids = [[50,45,20],[95,37,53],[45,23,12]]
print(obj.maxHeight(cuboids))
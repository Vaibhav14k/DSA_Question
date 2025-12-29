class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l=r=0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
            print("k:",k,"left:",l,"right:",r)
        return r-l+1


obj = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
nums = [0,0,0]
k = 2
print(obj.longestOnes(nums,k))
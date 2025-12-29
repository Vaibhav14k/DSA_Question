class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        i=0
        n = len(nums)
        if not nums or n==1:
            return []
        while i<n:
            j = nums[i]-1
            if nums[j] != nums[i]:
                nums[j],nums[i] = nums[i],nums[j]
            else:
                i+=1
        print(nums)
        duplicates = []
        for i in range(n):
            if nums[i] != i+1:
                duplicates.append(nums[i])
        print(duplicates)
        return (duplicates)

obj = Solution()
nums = [4,3,2,7,8,2,3,1]
nums = [1,1,2]
obj.findDuplicates(nums)
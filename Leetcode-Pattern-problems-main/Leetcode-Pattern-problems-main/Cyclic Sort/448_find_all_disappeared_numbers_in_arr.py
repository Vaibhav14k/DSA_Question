class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        i=0
        n = len(nums)
        while i<n:
            j=nums[i]-1
            if nums[j] != nums[i]:
                nums[j],nums[i] = nums[i], nums[j]
            else:
                i+=1
        print(nums)
        missing = []
        for i in range(n):
            if nums[i] != i+1:
                missing.append(i+1)
        print(missing)
        return missing


obj = Solution()
nums = [4,3,2,7,8,2,3,1]
print(obj.findDisappearedNumbers(nums))
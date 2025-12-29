class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<=1:
            return
        first = 0
        second =1
        while second<n:
            if nums[first]==0 and nums[second] !=0:
                nums[first],nums[second] = nums[second], nums[first]
            elif nums[first]==0 and nums[second]==0:
                # first+=1
                second+=1
            else:
                first+=1
                second+=1
        print(nums)


obj = Solution()
nums = [0,1,0,3,12]
nums = [0,0,1]
nums = [1,0]
obj.moveZeroes(nums)
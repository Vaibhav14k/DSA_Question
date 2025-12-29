class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        index = 2
        for i in range(2, n):
            print(nums)
            if nums[i] != nums[index - 2]:
                nums[index ] = nums[i]
                index += 1
        return index

obj = Solution()
nums = [1,1,1,2,2,2,3]
print(obj.removeDuplicates(nums))
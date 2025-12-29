class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left=0
        right=1
        count=1
        print("nums-->",nums)
        while right<len(nums):
            if nums[left]==nums[right]:
                nums[right]="_"
                print("nums->",nums)
                right+=1
            else:
                nums[count]=nums[right]
                if nums[count]==nums[right]and count!=right:
                    nums[right]="_"
                count+=1
                print("nums--->",nums)
                left+=1
                right+=1
        return count

obj = Solution()
nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
print(obj.removeDuplicates(nums))
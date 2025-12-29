class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        count = 0
        left,right = 0,len(nums)-1
        while left< right:
            print(nums)
            s = nums[left] + nums[right]
            if s >k:
                right -=1
            elif s <k:
                left +=1
            else:
                print('left: ',left,'right: ',right)
                count +=1
                left,right = left+1,right-1
        return count

obj = Solution()
nums = [1,2,3,4]
k = 5
nums = [3,1,3,4,3]
k = 6
nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
print(obj.maxOperations(nums,k))
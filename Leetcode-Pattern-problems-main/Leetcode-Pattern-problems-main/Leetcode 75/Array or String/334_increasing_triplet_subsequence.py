class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')

        for num in nums:
            if num<=first:
                first = num
            elif num<=second:
                second = num
            else:
                return True
        return False


obj = Solution()
nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
nums = [2,4,-2,-3]
nums = [20,100,10,12,5,13]
print(obj.increasingTriplet(nums))
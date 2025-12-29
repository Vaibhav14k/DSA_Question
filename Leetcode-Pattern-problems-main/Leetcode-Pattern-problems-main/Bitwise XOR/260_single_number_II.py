class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            ones ^= (num & ~twos)
            print('ones-->',ones,end=" ")
            twos ^= (num & ~ones)
            print('twos-->',twos)

        # Easy approach is
        '''
            for i in nums:
                if nums.count(i) == 1:
                    retunr i
        '''
        return ones

obj = Solution()
nums = [2,2,3,2]
# nums = [0,1,0,1,0,1,99]
print(obj.singleNumber(nums))
        
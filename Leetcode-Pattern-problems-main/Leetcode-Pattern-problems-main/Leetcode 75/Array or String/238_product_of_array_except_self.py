class Solution(object):
    def productExceptSelf(self, nums):
        total_product = 1
        zero_count = 0
        
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1
        result = []
        if zero_count > 1:
            return [0] * len(nums)
        for num in nums:
            if num != 0:
                if zero_count == 1:
                    result.append(0)
                else:
                    result.append(total_product // num)
            else:
                result.append(total_product)
        
        return result

obj = Solution()
nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
nums = [0,0]
print(obj.productExceptSelf(nums))
class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        if len(nums)==1:
            return sum(nums)
        subarray = []
        for i in range(len(nums)):
            subarray.append(nums[i])
            x = nums[i]
            for j in range(i+1,len(nums)):
                x += nums[j]
                subarray.append(x)
        subarray.sort()
        # print(subarray[left-1:right])
        ans = sum(subarray[left-1:right])
        if ans > 10**9+7:
            return int(ans%(10**9+7))
        return ans

obj = Solution()
nums = [1,2,3,4]
n = 4
left = 1
right = 5
print(obj.rangeSum(nums,n,left,right))
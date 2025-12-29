class Solution:
    def solve(self,nums1,nums2,index,prev_swapped,dp):
        if index>=len(nums1):
            return 0
        no_swap = float('inf')
        swap = float('inf')
        if dp[index][prev_swapped] != -1:
            return dp[index][prev_swapped]
        if nums1[index-1] < nums1[index] and nums2[index-1] < nums2[index]:
            no_swap = self.solve(nums1,nums2,index+1,0,dp)
        if nums2[index-1] < nums1[index] and nums1[index-1] < nums2[index]:
            nums1[index], nums2[index] = nums2[index], nums1[index]
            swap =self.solve(nums1,nums2,index+1,1,dp) + 1
            nums2[index], nums1[index] = nums1[index], nums2[index]
        dp[index][prev_swapped] = min(swap,no_swap)
        return dp[index][prev_swapped]
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        dp = [[-1,-1] for _ in range(n+1)]
        nums1.insert(0,-1)
        nums2.insert(0,-1)
        return self.solve(nums1,nums2,1,0,dp)

obj = Solution()
nums1 = [1,3,5,4]
nums2 = [1,2,3,7]
print(obj.minSwap(nums1, nums2))
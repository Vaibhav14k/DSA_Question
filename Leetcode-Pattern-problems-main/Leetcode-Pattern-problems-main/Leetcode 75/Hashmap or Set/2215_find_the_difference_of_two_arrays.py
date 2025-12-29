class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        ans0 = set(nums1).difference(nums2)
        print(ans0)
        ans1 = set(nums2).difference(nums1)
        print(ans1)
        ans = []
        ans.append(list(ans0))
        ans.append(list(ans1))
        return ans

obj = Solution()
nums1 = [1,2,3]
nums2 = [2,4,6]
print(obj.findDifference(nums1,nums2))
class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return sorted(arr) == sorted(target)

obj = Solution()
target = [1,2,3,4]
arr = [2,4,1,3]
print(obj.canBeEqual(target, arr))  # Output: True
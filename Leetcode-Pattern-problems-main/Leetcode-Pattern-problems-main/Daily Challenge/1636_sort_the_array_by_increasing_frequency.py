from typing import Counter,List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        print(counter)
        nums.sort(key=lambda x: (counter[x], -x))
        return nums

obj = Solution()
nums = [1,1,2,2,2,3]
nums = [2,3,1,3,2]
print(obj.frequencySort(nums))
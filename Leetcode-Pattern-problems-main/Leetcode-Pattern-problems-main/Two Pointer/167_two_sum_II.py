class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        if sum(numbers)<target:
            return []
        left=0
        right=len(numbers)-1
        print(right)
        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1


obj = Solution()
numbers = [2,7,11,15]
target = 9
print(obj.twoSum(numbers, target))
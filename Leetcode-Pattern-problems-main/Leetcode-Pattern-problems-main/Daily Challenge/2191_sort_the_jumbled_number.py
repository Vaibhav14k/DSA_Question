class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        arr = []
        i = 0
        while i<len(nums):
            num = str(nums[i])
            temp = ''
            for j in range(len(num)):
                temp += str(mapping[int(num[j])])
            arr.append((int(temp),nums[i]))
            i+=1
        print(arr)
        arr.sort(key= lambda x:x[0])

        return [num for new,num in arr]



obj = Solution()
mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]
mapping = [9,8,7,6,5,4,3,2,1,0]
nums = [0,1,2,3,4,5,6,7,8,9]
print(obj.sortJumbled(mapping, nums))
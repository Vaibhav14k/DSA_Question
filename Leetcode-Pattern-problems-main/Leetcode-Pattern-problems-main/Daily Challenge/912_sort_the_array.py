from typing import Counter
class Solution:
    ''' MERGE SORT
    def merge(self,arr, s, e):
        mid = (s + e) // 2
        l1 = mid - s + 1
        l2 = e - mid
        # print("l1-->", l1, "l2-->", l2)
        left = [0] * l1
        right = [0] * l2
        k = s
        for i in range(l1):
            left[i] = arr[k]
            k += 1
        k = mid + 1
        for i in range(l2):
            right[i] = arr[k]
            k += 1
        index1 = 0
        index2 = 0
        k = s

        while index1 < l1 and index2 < l2:
            if left[index1] <= right[index2]:
                arr[k] = left[index1]
                index1 += 1
            else:
                arr[k] = right[index2]
                index2 += 1
            k += 1
        while index1 < l1:
            arr[k] = left[index1]
            index1 += 1
            k += 1
        while index2 < l2:
            arr[k] = right[index2]
            index2 += 1
            k += 1

    def mergeSort(self,arr, s, e):
        if s >= e:
            return
        mid = (s + e) // 2
        self.mergeSort(arr, s, mid)
        self.mergeSort(arr, mid + 1, e)
        self.merge(arr, s, e)
        return arr
    
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        return self.mergeSort(nums, 0, len(nums) - 1)
    '''
    # Counting Sort 
    def sortArray(self, nums: list[int]) -> list[int]:
        counter = Counter(nums)
        minn = min(nums)
        maxx = max(nums)
        arr =[]
        for i in range(minn,maxx+1):
            if counter[i] > 0:
                arr.extend([i] * counter[i])
        return arr

nums = [5,2,3,1]
nums = [5,1,1,2,0,0]
nums = [-4,0,7,4,9,-5,-1,0,-7,-1]
obj = Solution()
print(obj.sortArray(nums))
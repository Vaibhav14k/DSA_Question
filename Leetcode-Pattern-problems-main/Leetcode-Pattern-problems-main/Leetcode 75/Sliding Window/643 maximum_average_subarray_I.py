class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        if n<k:
            avg =0
            for i in range(n):
                avg+=nums[i]/n
            return round(avg,4)
        start =0
        max_avg=0
        window_avg=0

        for i in range(k):
            window_avg+=nums[i]/k
        max_avg=window_avg
        print("Maximum average -->",max_avg)
        for i in range(k,n):
            window_avg += nums[i]/k - nums[start]/k
            max_avg = max(max_avg,window_avg)
            print("Maximum average -->",max_avg)
            start+=1
        print("Maximum average -->",max_avg)
        return round(max_avg,4)


nums = [3,3,4,3,0]
# nums = [1,12,-5,-6,50,3]
k = 3

obj = Solution()
print(obj.findMaxAverage(nums, k))
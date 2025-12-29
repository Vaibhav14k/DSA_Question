class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        n = len(arr)
        count = [1] * n
        for i in range(n):
            ele = arr[i] - difference
            j = i-1
            while j>=0:
                if arr[j]==ele:
                    break
                j-=1
            if j != -1:
                count[i] += count[j]
        print(count)
        return max(count)


arr = [1,5,7,8,5,3,4,2,1]
difference = -2
print(Solution().longestSubsequence(arr,difference))
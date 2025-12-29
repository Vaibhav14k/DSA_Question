class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            diff = prices[i] - mini
            ans = max(ans, diff)
            mini = min(mini,prices[i])
        return ans


obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))  
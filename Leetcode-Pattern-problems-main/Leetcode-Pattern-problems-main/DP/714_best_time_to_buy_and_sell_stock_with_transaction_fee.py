class Solution:
    def solve(self,prices,fee,index,can_buy,memo):
        if index == len(prices):
            return 0
        if memo[index][can_buy] != -1:
            return memo[index][can_buy]
        profit = 0
        if can_buy:
            buy_karo = -prices[index]  + self.solve(prices,fee,index+1,0,memo)
            skip_karo = 0 + self.solve(prices,fee,index+1,1,memo)
            profit = max(buy_karo,skip_karo)
        else:
            sell_karo = prices[index]  + self.solve(prices,fee,index+1,1,memo) - fee
            skip_karo = 0 + self.solve(prices,fee,index+1,0,memo)
            profit = max(sell_karo,skip_karo)
        memo[index][can_buy] = profit
        return memo[index][can_buy]
    def maxProfit(self, prices: list[int], fee: int) -> int:
        memo = [[-1 for _ in range(2)] for _ in range(len(prices))]
        return self.solve(prices,fee,0,1,memo)

obj = Solution()
prices = [1,3,2,8,4,9]
fee = 2
print(obj.maxProfit(prices,fee))
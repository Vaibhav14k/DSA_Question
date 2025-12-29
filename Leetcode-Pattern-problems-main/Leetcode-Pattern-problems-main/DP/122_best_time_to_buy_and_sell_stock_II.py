class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,prices,index,can_buy,memo):
        if index == len(prices):
            return 0
        if memo[index][can_buy] != -1:
            return memo[index][can_buy]
        profit = 0
        if can_buy:
            buy_karo = -prices[index] + self.solve(prices,index+1,0,memo)
            skip_karo = 0 + self.solve(prices,index+1,1,memo)
            profit = max(buy_karo,skip_karo)
        else:
            sell_karo = prices[index] + self.solve(prices,index+1,1,memo)
            skip_karo = 0 + self.solve(prices,index+1,0,memo)
            profit = max(sell_karo,skip_karo)
        memo[index][can_buy] = profit
        return memo[index][can_buy]
    def maxProfit(self, prices: list[int]) -> int:
        memo = [[-1 for _ in range(2)] for _ in range(len(prices))]
        return self.solve(prices,0,1,memo)
    '''
    def solve(self,prices):
        dp = [[0 for _ in range(2)] for _ in range(len(prices)+1)]
        curr = [0] * 2
        prev = [0] * 2
        for index in range(len(prices)-1,-1,-1):
            for can_buy in range(2):
                profit = 0
                if can_buy:
                    buy_karo = -prices[index] + prev[0]
                    skip_karo = 0 + prev[1]
                    profit = max(buy_karo,skip_karo)
                else:
                    sell_karo = prices[index] +prev[1]
                    skip_karo = 0 + prev[0]
                    profit = max(sell_karo,skip_karo)
                curr[can_buy] = profit
                prev = curr.copy()
        return prev[1]
    def maxProfit(self, prices: list[int]) -> int:
        return self.solve(prices)

obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))  
class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,prices,index,can_buy,memo,limit):
        if index == len(prices):
            return 0
        if limit==0:
            return 0
        if memo[index][can_buy][limit] != -1:
            return memo[index][can_buy][limit]
        profit = 0
        if can_buy:
            buy_karo = -prices[index] + self.solve(prices,index+1,0,memo,limit)
            skip_karo = 0 + self.solve(prices,index+1,1,memo,limit)
            profit = max(buy_karo,skip_karo)
        else:
            sell_karo = prices[index] + self.solve(prices,index+1,1,memo,limit-1)
            skip_karo = 0 + self.solve(prices,index+1,0,memo,limit)
            profit = max(sell_karo,skip_karo)
        memo[index][can_buy][limit] = profit
        return memo[index][can_buy][limit]

    def maxProfit(self, prices: list[int]) -> int:
        memo = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(len(prices))]
        return self.solve(prices,0,1,memo,2)
    '''
    ''' BOTTOM UP APPROACH
    def solve(self,prices):
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(len(prices)+1)]
        for index in range(len(prices)-1,-1,-1):
            for can_buy in range(2):
                for limit in range(1,3):
                    profit = 0
                    if can_buy:
                        buy_karo = -prices[index] + dp[index+1][0][limit]
                        skip_karo = 0 + dp[index+1][1][limit]
                        profit = max(buy_karo,skip_karo)
                    else:
                        sell_karo = prices[index] + dp[index+1][1][limit-1]
                        skip_karo = 0 + dp[index+1][0][limit]
                        profit = max(sell_karo,skip_karo)
                    dp[index][can_buy][limit] = profit
        return dp[index][can_buy][limit]
    '''
    def solve(self,prices):
        curr = [[0 for _ in range(3)] for _ in range(2)]
        next = [[0 for _ in range(3)] for _ in range(2)]
        for index in range(len(prices)-1,-1,-1):
            for can_buy in range(2):
                for limit in range(1,3):
                    profit = 0
                    if can_buy:
                        buy_karo = -prices[index] + next[0][limit]
                        skip_karo = 0 + next[1][limit]
                        profit = max(buy_karo,skip_karo)
                    else:
                        sell_karo = prices[index] + next[1][limit-1]
                        skip_karo = 0 + next[0][limit]
                        profit = max(sell_karo,skip_karo)
                    curr[can_buy][limit] = profit
            next = curr[:]
        return next[can_buy][limit]

    def maxProfit(self, prices: list[int]) -> int:
        return self.solve(prices)


obj = Solution()
print(obj.maxProfit(prices = [3,3,5,0,0,3,1,4]))  
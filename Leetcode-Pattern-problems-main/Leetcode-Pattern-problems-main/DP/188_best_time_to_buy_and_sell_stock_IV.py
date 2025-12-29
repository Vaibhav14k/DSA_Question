class Solution:
    ''' PREVIOUSLY OPTIMIZED SOLUTION
    def solve(self,k,prices):
        curr = [[0 for _ in range(k+1)] for _ in range(2)]
        next = [[0 for _ in range(k+1)] for _ in range(2)]
        for index in range(len(prices)-1,-1,-1):
            for can_buy in range(2):
                for limit in range(1,k+1):
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

    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.solve(prices,k)
    '''
    '''RECURSION + MEMOIZATION
    def solve(self,k,prices,index,operation_num,memo):
        if index==len(prices):
            return 0
        if operation_num == 2*k:
            return 0
        if memo[index][operation_num] != -1:
            return memo[index][operation_num]
        profit = 0
        if operation_num%2==0:
            buy_karo = -prices[index] + self.solve(k,prices,index+1,operation_num+1,memo)
            skip_karo = 0 + self.solve(k,prices,index+1,operation_num,memo)
            profit = max(buy_karo,skip_karo)
        else:
            sell_karo = prices[index] + self.solve(k,prices,index+1,operation_num+1,memo)
            skip_karo = 0 + self.solve(k,prices,index+1,operation_num,memo)
            profit = max(sell_karo,skip_karo)
        memo[index][operation_num] = profit
        return memo[index][operation_num]

    def maxProfit(self, k: int, prices: list[int]) -> int:
        memo = [[-1 for _ in range(2*k)] for _ in range(len(prices))]
        return self.solve(k,prices,0,0,memo)
    '''
    ''' BOTTOM UP APPROACH
    def solve(self,k,prices):
        dp = [[-1 for _ in range(2*k)] for _ in range(len(prices))]
        for index in range(len(prices)-1,-1,-1):
            for operation_num in range(2*k):
                profit = 0
                if operation_num%2==0:
                    buy_karo = -prices[index] + dp[index+1][operation_num+1]
                    skip_karo = 0 + dp[index+1][operation_num]
                    profit = max(buy_karo,skip_karo)
                else:
                    sell_karo = prices[index] + dp[index+1][operation_num+1]
                    skip_karo = 0 + dp[index+1][operation_num]
                    profit = max(sell_karo,skip_karo)
                dp[index][operation_num] = profit
        return dp[index][operation_num]

    def maxProfit(self, k: int, prices: list[int]) -> int:
        return self.solve(k,prices)
    '''
    def solve(self,k,prices):
        curr = [0 for _ in range(2*k +1)]
        next = [0 for _ in range(2*k +1)]
        for index in range(len(prices)-1,-1,-1):
            for operation_num in range(2*k):
                profit = 0
                if operation_num%2==0:
                    buy_karo = -prices[index] + next[operation_num+1]
                    skip_karo = 0 + next[operation_num]
                    profit = max(buy_karo,skip_karo)
                else:
                    sell_karo = prices[index] + next[operation_num+1]
                    skip_karo = 0 + next[operation_num]
                    profit = max(sell_karo,skip_karo)
                curr[operation_num] = profit
            next = curr[:]
        return next[0]

    def maxProfit(self, k: int, prices: list[int]) -> int:
        return self.solve(k,prices)


obj = Solution()
k = 2
prices = [3,2,6,5,0,3]
print(obj.maxProfit(k,prices))  
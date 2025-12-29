from collections import deque
class Solution:
    ''' RECURSION + MEMOIZATION
        def solve(self,n,days,cost,index,dp):
        if index>=n:
            return 0
        
        if dp[index] != -1:
            return dp[index]
        
        # 1 Day pass 
        oneDay = self.solve(n,days,cost,index+1,dp) + cost[0]
        
        i = index
        while i<n and days[i]<days[index] + 7:
            i+=1
        
        # 7 Days pass
        sevenDay = self.solve(n,days,cost,i,dp) + cost[1]
        
        i = index
        while i<n and days[i]<days[index] + 30:
            i+=1
        
        # 30 Days pass
        thirtyDay = self.solve(n,days,cost,i,dp) + cost[2]

        dp[index] =  min(oneDay,min(sevenDay,thirtyDay))
        return dp[index]

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        n = len(days)
        dp = [-1] * (n+1)
        return self.solve(n,days,costs,0,dp)
    '''
    ''' TABULATION APPROACH
    def solve(self,n,days,cost):
        dp = [float('inf')] * (n+1)
        dp[n] = 0
        for k in range(n-1,-1,-1):
            # 1 Day pass 
            oneDay = dp[k+1] + cost[0]
            
            i = k
            while i<n and days[i]<days[k] + 7:
                i+=1
            
            # 7 Days pass
            sevenDay = dp[i] + cost[1]
            
            i = k
            while i<n and days[i]<days[k] + 30:
                i+=1
            
            # 30 Days pass
            thirtyDay = dp[i] + cost[2]

            dp[k] =  min(oneDay,min(sevenDay,thirtyDay))
        return dp[k]
    '''
    
    def solve(self,n,days,costs):
        ans = 0
        monthly = deque()
        weekly = deque()
        for day in days :
            # Remove expired days 
            while len(monthly)>0 and monthly[0][0] <= day - 30:
                monthly.popleft()
            while len(weekly)>0 and weekly[0][0] <= day - 7:
                weekly.popleft()
            
            # Push Current Days cost 
            weekly.append((day,ans+costs[1]))
            monthly.append((day,ans+costs[2]))

            # Update the answer 
            ans = min(ans + costs[0], min(monthly[0][1],weekly[0][1]))
        return ans 

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        n = len(days)
        return self.solve(n,days,costs)


obj = Solution()
days = [2,5]
costs = [1,4,25]
print(obj.mincostTickets(days, costs))
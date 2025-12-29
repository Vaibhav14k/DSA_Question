from typing import List

class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self, rating: List[int], index: int, count:int, last_rating: int, direction: int,memo) -> int:
        if count == 3:
            return 1
        if index >= len(rating):
            return 0
        if (index, count, last_rating, direction) in memo:
            return memo[(index, count, last_rating, direction)]
        # print("Index-->",index,"--","count-->",count)
        total = 0
        if (direction == 0 and rating[index] > last_rating) or \
                (direction == 1 and   rating[index] < last_rating):
                print("Include ==> Index-->",index,"--","count-->",count,"num-->",rating[index])
                total += self.solve(rating, index+1, count + 1, rating[index],direction)
        print("Exclude ==> Index-->",index,"--","count-->",count,"num-->",rating[index])
        total += self.solve(rating, index+1, count, last_rating,direction)
        memo[(index, count, last_rating, direction)] = total
        return memo[(index, count, last_rating, direction)]

    def numTeams(self, rating: List[int]) -> int:
        memo = {}
        return self.solve(rating, 0,0,float('-inf'), 0,memo) + self.solve(rating, 0,0,float('inf'), 1,memo)
    '''

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0
        
        dp_inc = [0] * n
        dp_dec = [0] * n
        
        for i in range(n):
            for j in range(i):
                if rating[j] < rating[i]:
                    dp_inc[i] += 1
                elif rating[j] > rating[i]:
                    dp_dec[i] += 1
        
        teams = 0
        for k in range(n):
            for j in range(k):
                if rating[j] < rating[k]:
                    teams += dp_inc[j]
                elif rating[j] > rating[k]:
                    teams += dp_dec[j]
        
        return teams

obj = Solution()
rating = [2,5,3,4,1]
print(obj.numTeams(rating))
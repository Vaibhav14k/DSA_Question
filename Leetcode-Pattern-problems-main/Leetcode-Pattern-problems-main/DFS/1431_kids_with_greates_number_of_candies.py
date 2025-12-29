class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans = []
        maxx = max(candies)
        i = 0
        for i in candies:
            if i+extraCandies < maxx:
                ans.append(False)
            else:
                ans.append(True)
        print(ans)
        return ans

obj = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(obj.kidsWithCandies(candies,extraCandies))
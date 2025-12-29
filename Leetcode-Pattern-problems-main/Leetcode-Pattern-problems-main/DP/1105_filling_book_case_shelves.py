class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n+1)
        for i,(w,h) in enumerate(books,1):
            dp[i] = dp[i-1] + h
            for j in range(i-1,0,-1):
                w += books[j-1][0]
                if w>shelfWidth:
                    break
                h = max(h,books[j-1][1])
                dp[i] = min(dp[i],dp[j-1]+h)
        return dp[n]

obj = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4
print(obj.minHeightShelves(books,shelfWidth))  
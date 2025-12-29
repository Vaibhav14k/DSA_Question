from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        n = len(envelopes)
        if (n == 0):
            return 0
        envelopes.sort(key=lambda x: (x[0],-x[1]))
        ans = []
        ans.append(envelopes[0][1])
        for i in range(1,n):
            if  envelopes[i][1] > ans[-1]:
                ans.append(envelopes[i][1])
            else:
                idx1 = bisect_left(ans, envelopes[i][1])
                ans[idx1] = envelopes[i][1]
        return len(ans)

obj = Solution()
envelopes = [[5,4],[6,4],[6,7],[2,3]]
envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
print(obj.maxEnvelopes(envelopes))
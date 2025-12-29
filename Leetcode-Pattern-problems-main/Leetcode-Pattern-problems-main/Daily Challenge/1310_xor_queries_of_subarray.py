class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        prefix = [] 
        for i in arr:
            if prefix:
                prefix.append(prefix[-1] ^ i)
            else: 
                prefix.append(i)
        print(prefix)
        n = len(queries)
        sol = [0] * n
        for i in range(n):
            if queries[i][0] == 0:
                sol[i] = prefix[queries[i][1]]
            else:
                sol[i] = prefix[queries[i][1]] ^ prefix[queries[i][0]-1]
        return sol

obj = Solution()
arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(obj.xorQueries(arr, queries)) 
# Output: [2,7,14,8] 
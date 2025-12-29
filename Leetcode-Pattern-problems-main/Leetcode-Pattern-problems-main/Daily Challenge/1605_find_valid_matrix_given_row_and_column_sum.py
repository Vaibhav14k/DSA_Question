class Solution:
    def restoreMatrix(self, rowSum:list[int], colSum:list[int]) ->list[list[int]]:
        m = len(rowSum) 
        n = len(colSum)
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                value = min(rowSum[i],colSum[j])
                matrix[i][j] = value

                rowSum[i] -= value
                colSum[j] -= value

                if rowSum[i] == 0:
                    break
                if colSum[j] == 0:
                    continue
        return matrix
    

rowSum = [5,7,10]
colSum = [8,6,8]
print(Solution().restoreMatrix(rowSum,colSum))

class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        minn = []
        maxx = []
        for i  in range(m):
            minn.append(min(matrix[i]))
        for j in range(n):
            maxx.append(max([matrix[i][j] for i in range(m)]))
        print(maxx,minn)
        return list(set(minn) & set(maxx))

obj = Solution()
matrix = [[3,7,8],[9,11,13],[15,16,17]]
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(obj.luckyNumbers(matrix))
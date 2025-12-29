class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        ans = []
        totalCells = rows * cols
        steps = 1 
        i, j = rStart, cStart

        ans.append([i, j])
        count = 1 

        while count < totalCells:
            for _ in range(steps):
                j += 1
                if 0 <= i < rows and 0 <= j < cols:
                    ans.append([i, j])
                    count += 1

            for _ in range(steps):
                i += 1
                if 0 <= i < rows and 0 <= j < cols:
                    ans.append([i, j])
                    count += 1

            steps += 1

            for _ in range(steps):
                j -= 1
                if 0 <= i < rows and 0 <= j < cols:
                    ans.append([i, j])
                    count += 1

            for _ in range(steps):
                i -= 1
                if 0 <= i < rows and 0 <= j < cols:
                    ans.append([i, j])
                    count += 1

            steps += 1

        return ans

rows = 5
cols = 6
rStart = 1
cStart = 4
obj = Solution()
print(obj.spiralMatrixIII(rows, cols, rStart, cStart))  
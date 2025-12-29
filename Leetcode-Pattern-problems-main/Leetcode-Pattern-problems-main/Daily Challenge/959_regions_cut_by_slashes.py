class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        rows, cols = len(grid),len(grid[0])
        rows2, cols2 = 3 * rows, 3 * cols
        grid2 = [[0] * cols2 for _ in range(rows2)]

        # 3 * 3 Grid 
        for r  in range(rows):
            for c in range(cols):
                r2, c2 = 3 * r, 3 * c
                if grid[r][c] == '/':
                    grid2[r2][c2 + 2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2] = 1
                elif grid[r][c] == '\\':
                    grid2[r2][c2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2 + 2] = 1
        print(grid2)

        def dfs(r,c,visited):
            if (r<0 or c<0 or r==rows2 or c==cols2 or grid2[r][c] != 0 or (r,c) in visited):
                return 0
            visited.add((r,c))
            neighbours = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for nr,nc in neighbours:
                dfs(nr,nc,visited)
        visited = set()
        res = 0
        
        # Traversal from each r,c
        for r in range(rows2):
            for c in range(cols2):
                if grid2[r][c] == 0 and (r,c) not in visited:
                    res += 1
                    dfs( r, c, visited)
        return res

obj = Solution()
grid = ["/\\","\\/"]
print(obj.regionsBySlashes(grid)) 
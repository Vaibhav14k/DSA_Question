from typing import DefaultDict

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
        print(dist)

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        print(dist)
        
        # Floyd-Warshall algorithm to compute all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        print(dist)
        min_count = n
        city = -1
        
        for i in range(n):
            count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if count < min_count or (count == min_count and i > city):
                min_count = count
                city = i
        return city

obj = Solution()
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(obj.findTheCity(n, edges, distanceThreshold))

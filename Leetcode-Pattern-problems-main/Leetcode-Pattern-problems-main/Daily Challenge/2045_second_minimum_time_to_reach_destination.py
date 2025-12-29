from collections import defaultdict, deque

class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        res = -1
        q = deque([(1, 0)])  # (node, curr_time)
        visited = defaultdict(list)
        visited[1].append(0)
        
        while q:
            node, curr_time = q.popleft()
            
            # Calculate next time considering the traffic signal
            if (curr_time // change) % 2 == 1:
                curr_time += change - (curr_time % change)
            next_time = curr_time + time
            
            for nei in adj[node]:
                if nei == n:
                    if res == -1:
                        res = next_time  # First time reaching n
                    elif next_time > res:
                        return next_time  # Second time reaching n
                if len(visited[nei]) < 2:
                    if len(visited[nei]) == 0 or visited[nei][0] != next_time:
                        visited[nei].append(next_time)
                        q.append((nei, next_time))
        return -1

# Test case
n = 5
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
time = 3
change = 5
obj = Solution()
print(obj.secondMinimum(n, edges, time, change)) 

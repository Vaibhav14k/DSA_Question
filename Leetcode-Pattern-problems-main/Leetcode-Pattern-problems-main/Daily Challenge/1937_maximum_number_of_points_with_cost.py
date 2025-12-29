class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [0] * n

        # Initialize dp with the first row
        for j in range(n):
            dp[j] = points[0][j]

        # Traverse through each row
        for i in range(1, m):
            leftMax = [0] * n
            rightMax = [0] * n
            newDp = [0] * n

            # Calculate left max
            leftMax[0] = dp[0]
            for j in range(1, n):
                leftMax[j] = max(leftMax[j - 1], dp[j] + j)

            # Calculate right max
            rightMax[n - 1] = dp[n - 1] - (n - 1)
            for j in range(n - 2, -1, -1):
                rightMax[j] = max(rightMax[j + 1], dp[j] - j)

            # Calculate new DP for the current row
            for j in range(n):
                newDp[j] = max(leftMax[j] - j, rightMax[j] + j) + points[i][j]
            print("left max -->",leftMax)
            print("right max -->",rightMax)
            print("New DP -->",newDp)
            dp = newDp

        return max(dp)


obj = Solution()
points = [[1,2,3],[1,5,1],[3,1,1]]
points = [[1,5],[2,3],[4,2]]
print(obj.maxPoints(points))  
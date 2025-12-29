# ! For 1-D array
arr = [2, 3, -1, 5, 4]
n = len(arr)

prefix_sum = [0] * (n)
prefix_sum[0] = arr[0]

for i in range(1,n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
print(prefix_sum)

# Find the sum between [2,4] limits encluded
print(prefix_sum[4] - prefix_sum[2-1])


# For 2-D array
arr = [[1, 2, 3], [4, 5, 6],[7,8,9]]
n = len(arr)
m = len(arr[0])
prefix_sum = [[0 for _ in range(m+1)]for _ in range(n+1)]

# Calculation of prefix sum matrix
for i in range(1,n+1):
    for j in range(1,m+1):
        prefix_sum[i][j] = arr[i-1][j-1]  + prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1]
print(prefix_sum)

# to calculate prefix sum from (1,2) to (3,3)
sol = prefix_sum[3][3] - prefix_sum[0][3] - prefix_sum[3][1] - prefix_sum[0][1]
print(sol)
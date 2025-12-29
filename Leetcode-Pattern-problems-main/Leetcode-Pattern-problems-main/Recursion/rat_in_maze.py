def isSafe(m,n,x,y,visited):
    if (x>=0 and x<n) and (y>=0 and y<n) and m[x][y] and not visited[x][y]:
        return True
    return False

def solve(m,n,x,y,ans,v,path):
    if x==n-1 and y==n-1:
        ans.append(path)
        return
    v[x][y]=True
    # down
    newx = x+1
    newy = y
    if(isSafe(m,n,newx,newy,v)):
        solve(m,n,newx,newy,ans,v,path+"D")
    # left
    newx = x
    newy = y-1
    if(isSafe(m,n,newx,newy,v)):
        solve(m,n,newx,newy,ans,v,path+"L")
    # right
    newx = x
    newy = y+1
    if(isSafe(m,n,newx,newy,v)):
        solve(m,n,newx,newy,ans,v,path+"R")
    # up
    newx = x-1
    newy = y
    if(isSafe(m,n,newx,newy,v)):
        solve(m,n,newx,newy,ans,v,path+"U")
    
    v[x][y]=False




def rat_in_maze(matrix,n):
    if(matrix[0][0]==0):
        return []
    srcx = 0
    srcy = 0
    ans = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    path = ""
    solve(matrix,n,srcx,srcy,ans,visited,path)
    return ans

matrix = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
n = len(matrix)
print(rat_in_maze(matrix, n))

import sys
input = sys.stdin.readline

n = int(input())
mountains = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    a = input().split()
    for j in range(n):
        mountains[i][j] = int(a[j])

maxHeigh = 0
maxIslandNumber = 0

def dfs(row, col, heigh, visited):
    if (row >= n or row < 0 or col >= n or col < 0 or visited[row][col] == True or mountains[row][col] <= heigh):
        return
    
    visited[row][col] = True
    dfs(row - 1, col, heigh, visited)
    dfs(row, col - 1, heigh, visited)
    dfs(row + 1, col, heigh, visited)
    dfs(row, col + 1, heigh, visited)

for h in range(11):
    visited = [[False for i in range(n)] for j in range(n)]
    numberOfIsland = 0

    for j in range(n):
        for k in range(n):
            if (visited[j][k] == False and mountains[j][k] > h):
                dfs(j, k, h, visited)
                numberOfIsland += 1
    
    if (numberOfIsland > maxIslandNumber):
        maxIslandNumber = numberOfIsland
        maxHeigh = h


print(maxHeigh)

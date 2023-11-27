import sys
input = sys.stdin.readline

a = []
M, N = [int(i) for i in input().split()]
for i in range(N):
    a.append([int(j) for j in input().split()])
visted = [[False for i in range(M)] for j in range(N)]
edges = [[False for i in range(M)] for j in range(N)]

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def inBound(i, j):
    return i >= 0 and i < N and j >= 0 and j < M

def isEdge(i, j):
    return i == 0 or j == 0 or i == N-1 or j == M-1

def bfs(h, w):
    isIsland = True
    q = []
    q.insert(0, [h, w])
    while(len(q) > 0):
        cn = q.pop()
        if (isEdge(cn[0], cn[1])):
            isIsland = False

        for i in range(4):
            curI = cn[0] + di[i]
            curJ = cn[1] + dj[i]
            if (inBound(curI, curJ) == False):
                continue

            if (a[curI][curJ] == 0 and visted[curI][curJ] == False):
                q.insert(0, [curI, curJ])
                visted[curI][curJ] = True
        
    return isIsland

ans = 0
for i in range(N):
    for j in range(M):
        if (visted[i][j] == False and a[i][j] == 0):
            visted[i][j] = True
            isIsolated = bfs(i, j)
            if (isIsolated == True):
                ans += 1
print(ans)

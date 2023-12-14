import sys
input = sys.stdin.readline

R, C, N = [int(i) for i in input().split()]
island = []
dist = []
shrine = []
for i in range(R):
    island.append(input().replace('\n', ''))
    dist.append([-1 for i in range(C)])

for i in range(R):
    for j in range(C):
        if (island[i][j] != '#' and island[i][j] != '.'):
            shrine.append([i, j])

def inBound(x, y):
    return x >= 0 and x < R and y >= 0 and y < C


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x1, y1, x2, y2):
    visited = [[False for i in range(C)] for j in range(R)]
    q = [[x1, y1, 0]]
    visited[x1][y1] = True
    while(q):
        cur = q.pop(0)
        if (cur[0] == x2 and cur[1] == y2):
            return cur[2]
        
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if (inBound(nx, ny) == False or visited[nx][ny] == True or island[nx][ny] == '#'):
                continue
            visited[nx][ny] = True
            q.append([nx, ny, cur[2] + 1])
    return -1

ans = sys.maxsize
def permute(step, n, k, arrOfIndex, checked, mapOfShrine):
    global ans
    if (step == k):
        tempAns = 0
        for i in range(1, N):
            tempAns += mapOfShrine[arrOfIndex[i-1]][arrOfIndex[i]]
        ans = min(ans, tempAns)


    else:
        for i in range(n):
            if checked[i] == False:
                arrOfIndex[step] = i
                checked[i] = True
                permute(step + 1, n, k, arrOfIndex, checked, mapOfShrine)
                checked[i] = False

def main():
    global ans
    mapOfShrine = [[0 for i in range(N)] for j in range(N)]
    for i in range(N-1):
        for j in range(N):
            ret = bfs(shrine[i][0], shrine[i][1], shrine[j][0], shrine[j][1])
            if (ret == -1):
                ans = -1
                break
            else:
                mapOfShrine[i][j] = ret
                mapOfShrine[j][i] = ret

        if (ans == -1):
            break
    if (ans != -1):
        checked = [False for i in range(N)]
        arrOfIndex = [0 for i in range(N)]
        permute(0, N, N, arrOfIndex, checked, mapOfShrine)
    print(ans)

main()
import sys
input = sys.stdin.readline

R, C, N, S, F = [int(i) for i in input().split()]
island = []
dist = []
shrine = []
iShrineWoSF = []
iShrineSF = []
for i in range(R):
    island.append(input().replace('\n', ''))
    dist.append([-1 for i in range(C)])

index = 0
for i in range(R):
    for j in range(C):
        if (island[i][j] != '#' and island[i][j] != '.'):
            shrine.append([i, j])
            if (int(island[i][j]) == S):
                iShrineSF.insert(0, index)
            elif (int(island[i][j]) == F):
                iShrineSF.append(index)
            else:
                iShrineWoSF.append(index)
    index+=1

def inBound(x, y):
    return x >= 0 and x < R and y >= 0 and y < C


dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

def bfs(x1, y1, x2, y2):
    visited = [[False for i in range(C)] for j in range(R)]
    q = [[x1, y1, 0]]
    visited[x1][y1] = True
    while(q):
        cur = q.pop(0)
        if (cur[0] == x2 and cur[1] == y2):
            return cur[2]
        
        for i in range(8):
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
        # print(mapOfShrine)
        # print(iShrineWoSF)
        for i in range(1, N-2):
            tempAns += mapOfShrine[iShrineWoSF[arrOfIndex[i-1]]][iShrineWoSF[arrOfIndex[i]]]
        # print(mapOfShrine[iShrineSF[0]][iShrineWoSF[arrOfIndex[1]]])
        # print(mapOfShrine[iShrineSF[1]][iShrineWoSF[arrOfIndex[N-3]]])
        tempAns += mapOfShrine[iShrineSF[0]][iShrineWoSF[arrOfIndex[1]]]
        tempAns += mapOfShrine[iShrineSF[1]][iShrineWoSF[arrOfIndex[N-3]]]
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
        checked = [False for i in range(N-2)]
        arrOfIndex = [0 for i in range(N-2)]
        if (N == 2):
            ans = mapOfShrine[0][1]
        elif (N == 3):
            ans = mapOfShrine[iShrineSF[0]][iShrineWoSF[0]] + mapOfShrine[iShrineSF[1]][iShrineWoSF[0]]
        else:    
            permute(0, N-2, N-2, arrOfIndex, checked, mapOfShrine)
    print(ans)

main()
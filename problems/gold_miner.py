import sys
input = sys.stdin.readline

N, M = [int(i) for i in input().split()]

arr = [['.' for i in range(M)] for j in range(N)]
goldArr = []
goldTotal = 0
for i in range(N):
    temp = input().split()
    for j in range(M):
        arr[i][j] = temp[j]
        if (temp[j] == 'G'):
            goldArr.append([i, j])
            goldTotal += 1
# print(goldArr)

def isBound(i, j):
    return (i >= 0 and i < N and j < M and j >= 0)

di = [0, 0, -1, 1]
dj = [-1, 1, 0 ,0]

dist = [[sys.maxsize for i in range(M)] for j in range(N)]
q = []
goldCur = 0

def clearData():
    dist = [[50 for i in range(M)] for j in range(N)]
    global q
    q = []
    global goldCur
    goldCur = 0

def exploit(h, w, d, val):
    global q
    global goldCur
    for i in range(-d, d+1, 1):
        for j in range(-d, d+1, 1):
            curI = h + i
            curJ = w + j
            if (isBound(curI, curJ) == False or dist[curI][curJ] <= val):
                continue
            if (arr[curI][curJ] == 'G'):
                goldCur += 1

            dist[curI][curJ] = val
            q.insert(0, [curI, curJ, val])

def isBoom(h, w):
    return arr[h][w] != '.' and arr[h][w] != 'G'

def bfs(h, w):
    global q
    global goldCur
    exploit(h, w , 1, 1)
    while(len(q) > 0 and goldCur < goldTotal):
        cn = q[len(q) - 1]
        q.pop()
        for i in range(4):
            curI = cn[0] + di[i]
            curJ = cn[1] + dj[i]
            if (isBound(curI, curJ) == False or dist[curI][curJ] <= cn[2]+1):
                continue

            dist[curI][curJ] = cn[2]+1
            q.insert(0, [curI, curJ, cn[2]+1])
            if (arr[curI][curJ] == 'G'):
                goldCur += 1

        if (goldCur == goldTotal):
            break
        if (isBoom(cn[0], cn[1])):
            exploit(cn[0], cn[1], int(arr[cn[0]][cn[1]]), cn[2]+1)

ans = sys.maxsize
for i in range(N):
    for j in range(M):
        clearData()
        bfs(i, j)
        time = 0
        for gold in goldArr:
            time = max(time, dist[gold[0]][gold[1]])
        ans = min(ans, time)

print(ans)

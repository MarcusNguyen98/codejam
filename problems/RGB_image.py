import sys
input = sys.stdin.readline

N, M = [int(i) for i in input().split()]

arr = []
visited = [[False for i in range(M)] for j in range(N)]
largeG = 0
for i in range(N):
    arr.append(input().replace('\n', ''))


def inBound(x, y):
    return x >= 0 and x < N and y >= 0 and y < M

xi = [-1, 1, 0, 0]
yi = [0, 0, -1, 1]

arrC = [[0, 0, 'R'], [0, 0, 'G'], [0, 0, 'B']]
def cal(color, large):
    if (color == 'R'):
        arrC[0][0] += 1
        arrC[0][1] = max(arrC[0][1], large)
    if (color == 'G'):
        arrC[1][0] += 1
        arrC[1][1] = max(arrC[1][1], large)
    if (color == 'B'):
        arrC[2][0] += 1
        arrC[2][1] = max(arrC[2][1], large)

def dfs(x, y, color, visited):
    if (inBound(x, y) == False or arr[x][y] != color or visited[x][y] == True):
        return
    global largeG
    largeG += 1
    visited[x][y] = True
    for i in range(4):
        dfs(x + xi[i], y + yi[i], color, visited)


for i in range(N):
    for j in range(M):
        if (visited[i][j]):
            continue
        else:
            largeG = 0
            dfs(i, j, arr[i][j], visited)
            cal(arr[i][j], largeG)

arrT = []
maxB = 0
for i in arrC:
    if maxB < i[0]:
        arrT = []
        maxB = i[0]
        arrT.append(i)
    elif maxB == i[0]:
        arrT.append(i)

ansI = ''
ansM = 0
for i in range(len(arrT)):
    if (ansM < arrT[i][1]):
        ansI = arrT[i][2]
        ansM = arrT[i][1]

print(ansI)

import sys
input = sys.stdin.readline

N = int(input())

arr = [[0 for i in range(N)] for j in range(N)]
def draw(x, y, value):
    for i in range(y, N-y):
        if (arr[x][i] > 0): break
        arr[x][i] = value
        value += 1
    for i in range(x+1, N-x):
        if (arr[i][N-y-1] > 0): break
        arr[i][N-y-1] = value
        value += 1
    for i in range(N-y-2, y-1, -1):
        if (arr[N-x-1][i] > 0): break
        arr[N-x-1][i] = value
        value += 1
    for i in range(N-x-2, x, -1):
        if (arr[i][y] > 0): break
        arr[i][y] = value
        value += 1
    return value

ret=1
loop = N//2
if (N%2 > 0):
    loop+=1
for i in range(loop):
    ret = draw(i, i, ret)

for i in arr:
    print(*i)

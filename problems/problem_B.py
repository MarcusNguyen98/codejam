import sys
input = sys.stdin.readline

N = int(input())
a = []
for i in range(N):
    a.append([int(j) for j in input().split()])

ans = 0

maxSum = 0
sumOfA = 0
for i in range(N):
    tempI = 0
    tempJ = 0
    for j in range(N):
        tempI += a[i][j]
        tempJ += a[j][i]
        sumOfA += a[i][j]
    maxSum = max(maxSum, tempI, tempJ)

ans = maxSum*N - sumOfA

print(ans)

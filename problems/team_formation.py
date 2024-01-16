import sys
input = sys.stdin.readline

N = int(input())
X = [int(i) for i in input().split()]

X.sort()
ans = 0
cnt = 0
mS = X[0]
for i in range(N):
    cnt += 1
    if (cnt == mS):
        ans += 1
        cnt = 0
        if (i+1 < N):
            mS = X[i+1]
if (cnt > 0):
    ans += 1
print(ans)
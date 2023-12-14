import sys
input = sys.stdin.readline

N, X, M, K = [int(i) for i in input().split()]

gifts = [0 for i in range(N)]

ans = 0
for i in range(K):
    cur = M
    while(cur > 0):
        while(gifts[ans] >= X):
            ans += 1
            if (ans == N):
                ans = 0
        ans += 1
        if (ans == N):
            ans = 0
        while(gifts[ans] >= X):
            ans += 1
            if (ans == N):
                ans = 0
        cur -= 1

    gifts[ans] += 1
    if (i == K-1):
        break
    if (gifts[ans] == X):
        while(gifts[ans] >= X):
            ans -= 1
            if (ans == -1):
                ans = N - 1

print(ans+1)
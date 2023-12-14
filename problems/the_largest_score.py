import sys
input = sys.stdin.readline

N = int(input())
A = [int(i) for i in input().split()]

ans = 1
cnt = 1
delIndex = -1
for i in range(1, N):
    if (A[i] == A[i-1]):
        cnt += 1
    else:
        if ((i+1 < N) and A[i+1] == A[i-1]):
            if (delIndex != -1):
                cnt = i - delIndex - 1
            A[i] = A[i-1]
            delIndex = i
        else:
            cnt = 1
            delIndex = -1
    ans = max(ans, cnt)

print(ans)
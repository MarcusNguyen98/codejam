import sys
input = sys.stdin.readline

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

ans = 0
cnt = 0
for i in range(N):
    for j in range(N):
        for k in range(N-1):
            a = 0
            b = 0
            if (k >= i):
                a = A[k+1]
            else:
                a = A[k]
            
            if (k >= j):
                b = B[k+1]
            else:
                b = B[k]

            if (a == b):
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        cnt = 0
print(ans)
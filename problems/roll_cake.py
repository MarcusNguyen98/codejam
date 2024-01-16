import sys
input = sys.stdin.readline

N, M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

A.sort()
B = []
C = []
for i in A:
    if (i%10 == 0):
        B.append(i)
    else:
        C.append(i)

D = B + C
ans = 0
for i in D:
    if (M == 0):
        break
    if (i < 10):
        continue
    if (i%10 == 0):
        if (i//10 - 1 < M):
            ans += i//10
            M -= i//10 -1
        elif(i//10 - 1 == M):
            ans += i//10
            break
        else:
            ans += M
            break

    else:
        if (i//10 < M):
            ans += i//10
            M -= i//10
        elif(i//10 == M):
            ans += i//10
            break
        else:
            ans += M
            break
print(ans)
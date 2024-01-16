import sys
input = sys.stdin.readline

N = int(input())
A = [int(i) for i in input().split()]

A.sort(reverse=True)

ans = 0
sides = []
i = 0
while(i < N-1):
    if (abs(A[i] - A[i+1]) <= 1):
        sides.append(((A[i]+A[i+1])//2))
        i += 2
        if (len(sides) == 2):
            ans += sides[0]*sides[1]
            sides = []
    else:
        i += 1

print(ans)
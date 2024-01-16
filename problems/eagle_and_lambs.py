import sys
input = sys.stdin.readline

N = int(input())
A = [int(i) for i in input().split()]

days = 0
ans = 0
A.sort(reverse=True)
for i in A:
    if (i - days > 0):
        ans +=  i - days
        days += 1

print(ans)
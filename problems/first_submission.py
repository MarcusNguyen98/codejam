import sys
input = sys.stdin.readline

N = int(input())
temp = input().split()
arr = [int(temp[i]) for i in range(N)]

ans = 0
for i in range(1, N, 1):
    ans = max(ans, abs(arr[i] - arr[i-1]))

print(ans)
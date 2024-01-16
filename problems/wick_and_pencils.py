import sys
input = sys.stdin.readline

N = int(input())
A = [int(i) for i in input().split()]

A.sort()
def binarySearch(x, y):
    left = y + 1
    right = N - 1
    ans = 0
    while(left <= right):
        mid = (left + right) // 2
        if (A[x] + A[y] > A[mid]):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    if (ans == 0):
        return 0

    return ans - y

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        ans += binarySearch(i, j)


print(ans)
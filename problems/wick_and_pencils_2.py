import sys
input = sys.stdin.readline

N = int(input())
A = [int(i) for i in input().split()]

A.sort()
A.append(-1)
B = A.copy()
def permute(k, n):
    if (k==0 or k==n): return 1
    if (k==1): return n
    return permute(k-1, n-1) + permute(k, n-1)

def binarySearch(y):
    left = 0
    right = len(B) - 1
    ans = -1
    while(left <= right):
        mid = (left + right) // 2
        if (A[y]*2 > B[mid]):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans+1

ans = 0
cnt = 1
for i in range(N):
    if (A[i] == A[i+1]):
        cnt+=1
        
    else:
        if (cnt > 1):
            B = []
            for j in A:
                if (A[i] != j and j != -1):
                    B.append(j)

            cal = binarySearch(i)
            ans += permute(2, cnt) * cal
        cnt = 1

print(ans)
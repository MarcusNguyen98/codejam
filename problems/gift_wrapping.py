import sys
input = sys.stdin.readline

temp = input().split()

N = int(temp[0])
M = int(temp[1])
Q = int(temp[2])

A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
Q = [int(i) for i in input().split()]

K = [0 for i in range(N+2)]

for i in range(M):
    K[A[i]] += 1
    K[B[i]+1] -= 1
        
for i in range(1, N+1, 1):
    K[i] = K[i] + K[i-1]

K = sorted(K)
# print(K)
for i in Q:
    low = 0
    high = N+1
    mid = 0
    while (low <= high):
        mid = (low + high) // 2
        if (K[mid] == i):
            break
        elif (K[mid] > i):
            high = mid - 1
        else:
            low = mid + 1
    # print(mid)
    if (K[mid] >= i):
        while(mid - 1 >= 0 and K[mid-1] >= i):
            mid -= 1
        print(len(K)-mid)
    else:
        while(mid + 1 < len(K) and K[mid+1] < i):
            mid += 1
        print(len(K)-mid-1)
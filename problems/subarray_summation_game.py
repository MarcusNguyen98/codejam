import sys
input = sys.stdin.readline

MOD = 10**9 + 7
T = int(input())

def findSolution(n, m, A, XY):
    countA = [0 for _ in range(n+1)]

    for x, y in XY:
        # for i in range(x-1, y):
        countA[x-1] += 1
        countA[y] -= 1
    
    cnt = 0
    for i in range(n):
        cnt += + countA[i]
        countA[i] = cnt

    countASort = sorted(countA, reverse=True)
    max_cnt = 1
    tmp_cnt = 1
    for idx in range(1, n):
        if (countASort[idx] != countASort[idx-1]):
            tmp_cnt = 1
        else:
            tmp_cnt += 1
            max_cnt = (max_cnt * tmp_cnt) % MOD

    max_value = 0
    A = sorted(A, reverse=True)
    for idx in range(n):
        if (countASort[idx] > 0):
            max_value = (max_value + countASort[idx]*A[idx])
    return [max_value, max_cnt]


ans = []
for _ in range(T):
    n, m = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]

    XY = []
    for i in range(m):
        XY.append([int(j) for j in input().split()])

    
    ans.append(findSolution(n, m, A, XY))
for a in ans:
    print(*a)
import sys
input = sys.stdin.readline

N, L, K = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]
X.sort()
def possible(v):
    cn = 1
    length = X[0] + v*2
    for i in X:
        if (i > length):
            length = i + v*2
            cn += 1
        if (cn > K):
            # print('v = ' + str(v))
            return False
    return True

def binarySearch(low, high):
    ret = 0
    while(low <= high):
        mid = (low + high) // 2
        if (possible(mid)):
            high = mid - 1
            ret = mid
        else:
            low = mid + 1
            # print('low ' + str(low))
    return ret

def main():
    ans = 0
    if N > K:
        low = 1
        high = L // 2 + 1
        ans = binarySearch(low, high)
    print(ans)

main()

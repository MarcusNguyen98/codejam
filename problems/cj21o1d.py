import sys
input = sys.stdin.readline

T = int(input().strip())

def check(n, s, x, d):
    prev = x[0]

    for i in range(1, n):
        if prev + d <= x[i]:
            s -= 1
            prev = x[i]

            if (s == 1):
                print(d)
                return True
    return False

while T > 0:
    T -= 1

    n, s = [int(i) for i in input().strip().split()]
    x = [int(i) for i in input().strip().split()]
    x = sorted(x)

    ans = 0
    lo = 0
    high = x[n-1] - x[0]

    while (lo <= high):
        mid = (lo + high) // 2

        if check(n, s, x, mid):
            lo = mid + 1
            ans = mid
        else:
            high = mid - 1
    
    print(ans)
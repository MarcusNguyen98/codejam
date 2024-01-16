import sys
input = sys.stdin.readline

TC = int(input())

cnt = 0
ans = []

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

while(TC > 0):
    TC -= 1

    N, M, X = [int(i) for i in input().split()]
    g = gcd(N, M)
    ans.append(X // g)

for i in ans:
    print(i)
    
import sys
input = sys.stdin.readline

T = int(input().strip())

while T > 0:
    T -= 1

    n = int(input().strip())
    x = [int(i) for i in input().strip().split()]

    x = sorted(x)
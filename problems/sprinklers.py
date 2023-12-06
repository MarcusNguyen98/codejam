import sys
input = sys.stdin.readline

N, L, K = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]


def main():
    if N == K:
        print(0)
    else:
        X.sort()
        print(X)

main()

 
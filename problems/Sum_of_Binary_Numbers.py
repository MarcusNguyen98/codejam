import sys
input = sys.stdin.readline
from itertools import combinations


MAX = 10000 + 1
fact = [0, 1]

for i in range(2, MAX):
    fact.append(fact[-1] * i)


def combination(n, k):
    return fact[n] / (fact[k] * fact[n-k]) 

T = int(input().strip())

while T > 0:
    T -= 1

    n, x = [int(i) for i in input().strip().split()]
    v = [int(i) for i in input().strip().split()]



    print(ans)
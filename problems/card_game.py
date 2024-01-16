import sys
input = sys.stdin.readline
from itertools import permutations
ans = []
T = int(input())
 

def findWayToWin(n, Bob, Alice):
    Bob = int(min(Bob, Bob[::-1]))
    max_ans = 0
    for i in permutations(Alice, n):
        num = int(''.join(i))
        if (Bob > num):
            max_ans = max(max_ans, num)
    
    for i in permutations(Alice, n-1):
        num = int(''.join(i))
        if (Bob > num):
            max_ans = max(max_ans, num)

    return max_ans

for t in range(T):
    n = int(input())
    bob = input().strip()
    alice = input().strip()
    ans.append(findWayToWin(n, bob, alice))

for i in ans:
    print(i)
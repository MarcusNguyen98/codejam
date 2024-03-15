import sys
input = sys.stdin.readline
from itertools import combinations
ans = []
T = int(input().strip())
 

def findMinMax(k, Bob, Alice):
    pB = combinations(Bob, k)
    bobOptions = set()
    for i in pB:
        bobOptions.add(sum(i))
    
    pA = combinations(Alice, k)
    aliceOptions = set()
    for i in pA:
        aliceOptions.add(sum(i))
    
    aliceOptions = sorted(aliceOptions)
    bobOptions = sorted(bobOptions)

    maxAns = max(abs(aliceOptions[0]- bobOptions[-1]), abs(bobOptions[0] - aliceOptions[-1]))

    minAns = sys.maxsize
    
    for b in bobOptions:
        left = 0
        right = len(aliceOptions) - 1
        while(left <= right):
            mid = (left + right) // 2
            tmp = b - aliceOptions[mid]
            if (tmp == 0):
                minAns = 0
                break
            
            if (abs(tmp) < minAns):
                minAns = abs(tmp)

            if (tmp > 0):
                left = mid + 1
            else:
                right = mid - 1

        
        if (minAns == 0):
            break
    
    return str(abs(minAns)) + ' ' + str(maxAns)
    
for t in range(T):
    n, m, k = [int(i) for i in input().strip().split()]
    bob = [int(i) for i in input().strip().split()]
    alice = [int(i) for i in input().strip().split()]
    ans.append(findMinMax(k, bob, alice))

for i in ans:
    print(i)
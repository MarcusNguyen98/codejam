import sys
input = sys.stdin.readline
from itertools import combinations

TC = int(input().strip())

MAX = 10000
fact = [1, 1]
for i in range(2, MAX+1):
    fact.append(fact[-1] * i)



def compare(s1, s2, k):
    unique = [0] * 32
    cntUpper = 0
    for i in range(k):
        if (s1[i] >= 'A' and s1[i] <= 'Z'):
            cntUpper += 1
        num = ord(s1[i].lower()) - ord('a')
        unique[num] += 1
    
    for i in range(k):
        if (s2[i] >= 'A' and s2[i] <= 'Z'):
            cntUpper -= 1
        if (cntUpper < 0):
            return False

        num = ord(s2[i].lower()) - ord('a')
        unique[num] -= 1
        if (unique[num] < 0):
            return False
    
    if (cntUpper != 0):
        return False

    for i in unique:
        if (i > 0):
            return False
    
    return True


# print(compare('AtY', 'aTy', 3))
while (TC > 0):
    TC -= 1

    n, k = [int(i) for i in input().strip().split()]
    X = input().strip().split()

    ans = 0
    checked = [False] * n
    for i in range(n-1):
        if (checked[i] == True):
            continue
        checked[i] = True
        cnt = 1
        for j in range(i+1, n):
            if (checked[j] == True):
                continue

            if (compare(X[i], X[j], k)):
                # print(X[i] + ' ' + X[j])
                checked[j] = True
                cnt += 1

        if (cnt >= 2):
            # print(cnt)
            ans += (fact[cnt] // (fact[2] * fact[cnt-2]))
    
    print(ans)

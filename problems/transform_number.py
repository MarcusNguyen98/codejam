import sys
from math import sqrt
input = sys.stdin.readline

S, A, B = [int(i) for i in input().split()]
souc = [-1 for i in range(10000)]
def souocchung(a):
    if (souc[a] != -1):
        return souc[a]

    ans = 0
    for i in range(1, int(sqrt(a) + 1)):
        if (a % i == 0):
            if (a / i == i):
                ans += 1
            else:
                ans += 2
    souc[a] = ans
    return ans

def isTransform(a, b):
    strA = str(a)
    strB = str(b)
    difIndex = -1
    for i in range(4):
        if (strA[i] != strB[i]):
            if (difIndex != -1):
                return False
            else:
                difIndex = i
    
    divisorA = souocchung(a)
    divisorB = souocchung(b)

    return abs(divisorA-divisorB) <= 1 

def dfs(a, b):
    if (a == b):
        return 0
    dist = [-1 for i in range(10000)]
    dist[a] = 0
    st = [a]

    while(st):
        head = st.pop(0)
        sn = str(head)
        for i in range(4):
            for j in range(10):
                number = head - int(sn[i])*(10**(3-i)) + j*(10**(3-i))
                # print(number)
                if (number >= 1000 and dist[number] == -1 and isTransform(head, number)):
                    dist[number] = dist[head] + 1
                    st.append(number)
                    if (number == b):
                        return dist[b]

    return dist[b]

ansA = dfs(S, A)
ansB = dfs(S, B)
print(str(ansA) + ' ' + str(ansB))

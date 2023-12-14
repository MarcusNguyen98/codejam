import sys
input = sys.stdin.readline

S, A, B = [int(i) for i in input().split()]

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
    
    divisorA = 0
    for i in range(1, sqrt(a)):
        if (a % i == 0):
            divisorA += 1
    divisorB = 0
    for i in range(1, sqrt(b)):
        if (b % i == 0):
            divisorB += 1
    
    return abs(divisorA-divisorB) <= 1


def 

ansA = isTransform(S, A)
ansB = isTransform(S, B)
print(str(ansA) + ' ' + str(ansB))
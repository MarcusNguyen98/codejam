import sys
input = sys.stdin.readline

R, C, K = [int(i) for i in input().split()]

pos = {}
for i in range(K):
    temp = [int(i) for i in input().split()]
    if temp[0] in pos:
        pos[temp[0]].append(temp[1])
    else:
        pos[temp[0]] = [temp[1]]

tilesOfRow = (C//2)
tilesTotal = tilesOfRow * R
waysAns = 1

def cal(priv, cur):
    global tilesTotal
    tilesTotal += (cur - priv - 1) // 2
    if (cur - priv - 1 == 1 or (cur - priv - 1) % 2 == 0):
        return 1
    else:
        return ((cur - priv - 1) // 2) + 1

def powMod(x, y):
    res = 1
    x = x % 1000000007
    while (y > 0):
        if y & 1:
            res = res*x
        y = y//2
        x = (x*x) % 1000000007
    return res

priv = 0
for tmPos in pos:
    lst = pos[tmPos]
    lst.sort()

    for i in range(len(lst)):        
        if (priv == 0):
            tilesTotal -= tilesOfRow
            # if (C%2 == 1):
            #     waysAns = waysAns // ((C//2)+1)

        ways = cal(priv, lst[i])
        waysAns = (waysAns * ways) % 1000000007
        
        if (i == len(lst) - 1):
            priv = 0
            ways = cal(lst[i], C+1)
            waysAns = (waysAns * ways) % 1000000007
        else:
            priv = lst[i]

if (C%2 == 1):
    waysAns = (waysAns * powMod((C//2)+1, R-len(pos))) % 1000000007
print(str(tilesTotal) + ' ' + str(waysAns))

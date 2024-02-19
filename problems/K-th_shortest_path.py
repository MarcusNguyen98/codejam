import sys
input = sys.stdin.readline

fact = [1, 1]
multi_coff = [[[[0 for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]

def init():
    for i in range(2, 37):
        fact.append(fact[i-1]*i)
    
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    multi_coff[i][j][k][l] = fact[i+j+k+l] // fact[i] // fact[j] // fact[k] // fact[l]


def multi_cof(x, y):
    band = [0 for _ in range(4)]
    for i in range(4):
        xd = (x % (10 ** (i+1))) // (10 ** i)
        yd = (y % (10 ** (i+1))) // (10 ** i)
        band[i] = abs(xd-yd)
    
    return multi_coff[band[0]][band[1]][band[2]][band[3]]

def solve():
    L, K, x, y = [int(i) for i in input().split()]

    path = [x]
    remain = K
    while(x != y):
        cand = []
        for i in range(4):
            xd = (x % (10 ** (i+1))) // (10 ** i)
            yd = (y % (10 ** (i+1))) // (10 ** i)

            z = x
            if (xd > yd):
                z -= 10 ** i
            elif (xd < yd):
                z += 10 ** i
            
            if (z != x):
                cand.append(z)

        cand = sorted(cand)
        
        next = -1
        for i in cand:
            path_ways = multi_cof(i, y)
            if (path_ways >= remain):
                next = i
                break
            remain -= path_ways
        
        if (next == -1):
            print('NO')
            return
        
        path.append(next)
        x = next
    
    path= list(map(lambda x: str(x).zfill(L), path))
    path_str = " ".join(path)
    print(path_str)



init()
t = int(input())
for _ in range(t):
    solve()


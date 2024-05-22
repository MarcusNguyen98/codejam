import sys
input = sys.stdin.readline

T = int(input().strip())

while T > 0:
    T -= 1

    n = int(input().strip())
    A = [int(i) for i in input().strip().split()]

    dict = {}
    
    for e in A:
        if str(e) in dict:
                dict[str(e)] += 1
        else:
            dict[str(e)] = 1
    
    comp = []
    for i in range(10):
        comp.append(int('2020' + str(i) + '2021'))
    comp.append(20202021)
    comp.append(202021)

    ans = 0
    for e in dict:
        for c in comp:
            minus = c - int(e)
            if str(minus) in dict:
                ans += dict[e] * dict[str(minus)]

    print(ans//2)
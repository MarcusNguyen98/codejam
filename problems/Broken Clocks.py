import sys
input = sys.stdin.readline

TC = int(input().strip())

MAX = 86400

while (TC > 0):
    TC -= 1

    n = int(input().strip())
    T = input().strip().split()
    D = [int(i) % MAX for i in input().strip().split()]

    appeared = [-1] * MAX
    unique = []
    ans = 0
    for i in range(n):
        h, m, s = [int(_) for _ in T[i].split(':')]
        time = h*3600 + m*60 + s
        if (appeared[D[i]] == -1):
            appeared[D[i]] = time
            unique.append([time, D[i]])
        elif(appeared[D[i]] != time):
            break
    else:
        for i in range(1, MAX+1):
            base = (unique[0][0] + unique[0][1] * i) % MAX
            for j in range(1, len(unique)):
                target = (unique[j][0] + unique[j][1] * i) % MAX
                if (target != base):
                    break
            else:
                ans += 1
    
    print(ans)

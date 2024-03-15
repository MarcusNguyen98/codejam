import sys
input = sys.stdin.readline

TC = int(input())

while (TC > 0):
    TC -= 1

    X = [int(i) for i in input().strip().split()]
    if (X[5] > 0):
        X[8] += X[5]
        X[5] = 0
    first = ''
    last = ''
    cnt = 0
    for idx in range(8, -1, -1):

        while (X[idx] > 0):
            X[idx] -= 1

            if (cnt % 2 == 0):
                first += str(idx + 1) + ' '
            else:
                last = str(idx + 1) + ' ' + last
            
            cnt += 1

    print(first + last)
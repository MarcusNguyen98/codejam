import sys
input = sys.stdin.readline

map = [[0 for i in range(3)] for j in range(3)]

for i in range(3):
    a = input().split()
    for j in range(3):
        if (a[j] == 'X'):
            map[i][j] = 1
        else:
            map[i][j] = 0
ans = 0
for i in range (3):
    vertical = 0
    horizontal = 0
    for j in range (3):
        vertical += map[i][j]
        horizontal += map[j][i]

    diagonalLeft = map[0][0] + map[1][1] + map[2][2]
    diagonalRight = map[0][2] + map[1][1] + map[2][0]
    if (vertical == 3 or horizontal == 3 or diagonalLeft == 3 or diagonalRight == 3):
        print('X')
        ans = 1
        break
    elif (vertical == 0 or horizontal == 0 or diagonalLeft == 0 or diagonalRight == 0):
        print('O')
        ans = 1
        break

if (ans == 0):
    print('_')

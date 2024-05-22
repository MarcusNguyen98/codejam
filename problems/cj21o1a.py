import sys
input = sys.stdin.readline

T = int(input().strip())

Keyboard = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ''],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '', '', '']
]

ROW = 3
COL = 10

def bfs(xS, yS, end):
    if Keyboard[xS][yS] == end:
        return [1, xS, yS]
 
    dict = [[0 for _ in range(COL)] for _ in range(ROW)]
    queue = [[xS, yS]]
    dict[xS][yS] += 1
    while len(queue) > 0:
        # print(queue)
        # print(dict[1][7])
        head = queue.pop(0)
        x = head[0]
        y = head[1]
        
        # print(dict[1][8])
        # print(dict)
        if (y-1 >= 0 and dict[x][y-1] == 0 and Keyboard[x][y-1] != ''): 
            if Keyboard[x][y-1] == end:
                return [dict[x][y] + 2, x, y-1]
            else:
                dict[x][y-1] = dict[x][y] + 2
                queue.append([x, y-1])
        
        if (y + 1 < COL and dict[x][y+1] == 0 and Keyboard[x][y+1] != ''):
            if Keyboard[x][y+1] == end:
                return [dict[x][y] + 2, x, y+1]
            else:
                dict[x][y+1] = dict[x][y] + 2
                queue.append([x, y+1])
        
        if (x+1 < ROW):
            if Keyboard[x+1][y] == end:
                return [dict[x][y] + 2, x+1, y]
            elif dict[x+1][y] == 0 and Keyboard[x+1][y] != '':
                # print('-+' + str(dict[x][y]))
                dict[x+1][y] = dict[x][y] + 2
                queue.append([x+1, y])
            
            if y-1 >= 0:
                if Keyboard[x+1][y-1] == end:
                    # print(dict[x][y])
                    return [dict[x][y] + 2, x+1, y-1]
                elif dict[x+1][y-1] == 0 and Keyboard[x+1][y-1] != '':
                    # print(dict)
                    # print('--' + str(dict[x][y]))
                    dict[x+1][y-1] = dict[x][y] + 2
                    queue.append([x+1, y-1])
        
        if (x-1 >= 0):
            if Keyboard[x-1][y] == end:
                return [dict[x][y] + 2, x-1, y]
            elif dict[x-1][y] == 0 and Keyboard[x-1][y] != '':
                dict[x-1][y] = dict[x][y] + 2
                queue.append([x-1, y])
            
            if y+1 < COL:
                if Keyboard[x-1][y+1] == end:
                    return [dict[x][y] + 2, x-1, y+1]
                elif dict[x-1][y+1] == 0 and Keyboard[x-1][y+1] != '':
                    # print('-/' + str(dict[x][y]))
                    dict[x-1][y+1] = dict[x][y] + 2
                    queue.append([x-1, y+1])

while T > 0:
    T -= 1
    s = input().strip()
    if len(s) == 1:
        print(1)
        continue
    ans = 0
    xS = 0
    yS = 0
    found = False
    for i in range(ROW):
        for j in range(COL):
            if Keyboard[i][j] == s[0]:
                xS = i
                yS = j
                found = True
                break
        
        if found == True:
            break


    for i in range(1, len(s)):
        [step, newX, newY]= bfs(xS, yS, s[i])
        # print(Keyboard[xS][yS] + ' -> ' + Keyboard[newX][newY] + ' = ' + str(step))
        xS = newX
        yS = newY
        ans += step
    
    print(ans+1)

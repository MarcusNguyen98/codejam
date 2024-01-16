import sys
input = sys.stdin.readline

def scoreOfCharater(matrix, r, c):
    cnt = 0
    if (matrix[r][0] == 1 and matrix[r][1] == 1 and matrix[r][2] == 1):
        cnt += 1
    
    if (matrix[0][c] == 1 and matrix[1][c] == 1 and matrix[2][c] == 1):
        cnt += 1

    if (r == c and matrix[0][0] == 1 and matrix[1][1] == 1 and matrix[2][2] == 1):
        cnt += 1

    if (c == 2 - r and matrix[0][2] == 1 and matrix[1][1] == 1 and matrix[2][0] == 1):
        cnt += 1

    return cnt


def findScoreString(S, grid):
    matrix = [[0 for i in range(3)] for j in range(3)]

    score = ''
    for i in range(9):
        index = grid.find(S[i])
        row = index // 3
        col = index % 3
        matrix[row][col] = 1
        score += str(scoreOfCharater(matrix, row, col))
    return score

latestString = ''
def findLatestString(step, n, k, arrOfIndex, checked, S, grid, scoreCompare):
    global latestString
    if (latestString != ''):
        return

    if (step == k):
        matrix = [[0 for i in range(3)] for j in range(3)]
        tmp = ''
        for i in range(9):
            index = grid.find(S[arrOfIndex[i]])
            row = index // 3
            col = index % 3
            matrix[row][col] = 1
            if (scoreOfCharater(matrix, row, col) != int(scoreCompare[i])):
                return
            
            tmp += S[arrOfIndex[i]]

        latestString = tmp
                
    else:
        for i in range(n):
            if checked[i] == False:
                arrOfIndex[step] = i
                checked[i] = True
                findLatestString(step + 1, n, k, arrOfIndex, checked, S, grid, scoreCompare)
                checked[i] = False

T = int(input())
ans = []
for tc in range(T):
    S = input().replace('\n', '')
    grid = ''
    st = []
    for i in range(3):
        tmp = input().replace('\n', '')
        grid = grid + tmp

    ts = findScoreString(S, grid)
    
    latestString = ''
    arrOfIndex = [0 for i in range(9)]
    checked = [False for i in range(9)]
    findLatestString(0, 9, 9, arrOfIndex, checked, sorted(S), grid, ts)

    ts = ts + ' ' + latestString
    ans.append(ts)

for i in ans:
    print(i)
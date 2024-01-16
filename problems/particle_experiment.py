import sys
input = sys.stdin.readline

MOD = 10**9 + 7
T = int(input())
ans = []

def get_masks(base_mask, masks, start, end):
    for i in range(start, end - 1):
        switch = 3 << i
        if (switch & base_mask == 0):
            new_mask = base_mask | switch
            masks.append(new_mask)
            get_masks(new_mask, masks, i + 2, end)

def numberOfWays(S, R, C, K, XY):
    dp = [[0 for _ in range(2**C)] for _ in range(R+1)]
    
    initial_pattern = int(S.replace('+', '1').replace('-', '0'), 2)
    dp[0][initial_pattern] = 1

    arrOfXY = [['0' for _ in range(C)] for _ in range(R)]
    for x, y in XY:
        arrOfXY[x][y] = '1'
    
    for idx in range(R):
        base_mask = int(''.join(arrOfXY[idx]), 2)
        masks = [base_mask]
        get_masks(base_mask, masks, 0, C)

        for pattern, count in enumerate(dp[idx]):
            if count > 0:
                for mask in masks:
                    modified_mask = pattern ^ mask
                    dp[idx+1][modified_mask] = (dp[idx+1][modified_mask] + count) % MOD

    return dp[R][2**C - 1]

for tc in range(T):
    R, C, K = [int(i) for i in input().split()]
    S = input().strip()
    XY = []
    for k in range(K):
        XY.append([int(i) - 1 for i in input().split()])
    
    ans.append(numberOfWays(S, R, C, K, XY))

for i in ans:
    print(i)
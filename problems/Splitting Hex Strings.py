import sys
input = sys.stdin.readline

TC = int(input().strip())

def dfs(S, n, idx, prev_val):
    if (idx >= n):
        return 1
    
    ret = 0
    for i in range(idx, n):
        val = S[idx : i+1]
        if (int(val, 16) >= int(prev_val, 16)):
            ret += dfs(S, n, i+1, val)
    return ret

while TC > 0:
    TC -= 1

    S = input().strip()
    n = len(S)

    ans = dfs(S, n, 0, '0')
    print(ans)
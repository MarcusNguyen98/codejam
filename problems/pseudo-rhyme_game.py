import sys
input = sys.stdin.readline

T = int(input())

ans = []

for _ in range(T):
    n, L, F = [int(i) for i in input().split()]
    Ws = input().split()
    dict_Ws = {}
    cur_ans = 0
    for i in range(n):
        key = Ws[i][L - F:]
        
        if (dict_Ws.get(key) == None):
            dict_Ws[key] = 1
        else:
            dict_Ws[key] += 1

    for item in dict_Ws.values():
        cur_ans += item // 2 
    
    ans.append(cur_ans)

for i in ans:
    print(i)

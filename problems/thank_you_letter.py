import sys
input = sys.stdin.readline

N = int(input())
L = input().replace('\n', '')

pre = 0
isPrint = False
for i in range(1, N):
    # print(L[pre])
    # print(L[i])
    # print('----')
    if (L[pre] < L[i]):
        print(int(pre)+1)
        isPrint = True
        break
    else:
        pre = i
if (isPrint==False): print(N)
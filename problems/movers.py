import sys
input = sys.stdin.readline

items = [int(i) for i in input().split()]
weigh = [1, 2, 3, 4, 5]

ans = 0
weigh = 0
isRestart = False
while(True):
    for i in range(5, 0, -1):
        while (items[i-1] > 0):
            weigh += i
            if (weigh == 5):
                ans += 1
                weigh = 0
                items[i-1] -= 1
                isRestart = True
                break
            elif (weigh > 5):
                weigh -= i
                break
            else:
                items[i-1] -= 1
        if (isRestart):
            isRestart=False
            break
    if (weigh > 0):
        weigh = 0
        ans += 1

    isEmpty = True
    for i in items:
        if (i != 0):
            isEmpty = False
            break
    if (isEmpty == True):
        break
                
print(ans)


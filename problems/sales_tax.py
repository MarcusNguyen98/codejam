import sys
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    tmp = [_ for _ in input().split()]
    N = int(tmp[0])
    X = float(tmp[1])
    P = [0 for _ in range(N)]
    sumP = 0
    for i in range(N):
        P[i] = float(input())
        sumP += P[i]
    
    left = 0
    right = 10**4
    low_value = 0
    while (left <= right):
        mid = (left + right) // 2
        # print('left ' + str(left) + ' right ' + str(right) + ' mid ' + str(mid))
        # print(str(sumP * (1+ mid/100)))
        tax = round(sumP * (1 + mid/100), 4)
        tax_round = round(tax, 2)
        tax_high = tax_round if tax == tax_round else tax_round + 0.01
        tax_low = tax_round
        if (X <= int(tax_high) or X <= int(tax_low)):
            low_value = mid
            right = mid - 1
        else:
            left = mid + 1

    left = low_value
    right = 10**4
    high_value = 0
    while (left <= right):
        mid = (left + right) // 2
        # print('left ' + str(left) + ' right ' + str(right) + ' mid ' + str(mid))
        # print(str(sumP * (1+ mid/100)))
        
        tax = round(sumP * (1 + mid/100), 4)
        tax_round = round(tax, 2)

        tax_high = tax_round if tax_round > tax else tax
        tax_low = tax if tax_round > tax else tax_round

        if (X >= int(tax_high) or X >= int(tax_low)):
            high_value = mid
            left = mid + 1
        else:
            right = mid - 1

    ans.append([low_value, high_value])
    

for i in ans:
    print(*i)

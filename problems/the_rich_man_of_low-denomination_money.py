import sys
input = sys.stdin.readline

bills = [int(i) for i in input().split()]
moneys = [1, 2, 5, 10, 20, 50, 100, 200, 500]
total = int(input())

total = total//1000
M = [-1 for i in range(total + 1)]
M[0] = 0
tmpSum = 0
for i in range(9):
    tmpSum += moneys[i] * bills[i]
    for j in range(total+1):
        if (j > tmpSum):
            break
        if (j >= moneys[i] and M[j-moneys[i]] != -1):
            M[j] = max(M[j-moneys[i]]+1, M[j])

print(M[total])

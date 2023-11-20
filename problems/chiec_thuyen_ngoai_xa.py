import sys
input = sys.stdin.readline

n = int(input())
islands = [[0 for i in range(2)] for j in range(n)]

for i in range(n):
    a = input().split()
    for j in range(2):
        islands[i][j] = int(a[j])

tem = input().split()
A = [int(tem[0]), int(tem[1])]
tem = input().split()
B = [int(tem[0]), int(tem[1])]

ans = 99999999999999

# def binary(step, n, arr):
#     if (step == n):
#         return
#     else:
#         for i in range(2):
#             arr[step] = i
#             binary(step+1, n, arr)

def permute(step, n, k, arr, checked):
    global ans
    if (step == k):
        temp = 0
        # #A or B
        for i in range(1, n):
            temp = temp + (abs(islands[arr[i]][0] - islands[arr[i-1]][0]) + abs(islands[arr[i]][1] - islands[arr[i-1]][1])) * i
        tempA = temp + (abs(islands[arr[n-1]][0] - A[0]) + abs(islands[arr[n-1]][1] - A[1])) * n
        tempB = temp + (abs(islands[arr[n-1]][0] - B[0]) + abs(islands[arr[n-1]][1] - B[1])) * n

        if (tempA < ans):
            ans = tempA
        if (tempB < ans):
            ans = tempB

        tempA = 0
        for i in range(n-1):
            if i > 0:
                tempA = tempA + (abs(islands[arr[i]][0] - islands[arr[i-1]][0]) + abs(islands[arr[i]][1] - islands[arr[i-1]][1])) * i
            Aback = tempA + (abs(islands[arr[i]][0] - A[0]) + abs(islands[arr[i]][1] - A[1])) * (i+1)
            
            tempB = 0
            for j in range(i+2, n):
                tempB = tempB + (abs(islands[arr[j]][0] - islands[arr[j-1]][0]) + abs(islands[arr[j]][1] - islands[arr[j-1]][1])) * (j - i - 1)

            Bback = tempB + (abs(islands[arr[n-1]][0] - B[0]) + abs(islands[arr[n-1]][1] - B[1])) * (n-i-1)

            if (Aback + Bback < ans):
                ans = Aback + Bback

    else:
        for i in range(n):
            if checked[i] == False:
                arr[step] = i
                checked[i] = True
                permute(step + 1, n, k, arr, checked)
                checked[i] = False

  
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = i
checked = [False for i in range(n)]

permute(0, n, n, arr, checked)

print(ans)
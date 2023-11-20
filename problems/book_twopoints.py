n, t = input().split()
a = input().split()
t = int(t)
n = int(n)

b = [0 for i in range(n)]
b[0] = int(a[0])

for i in range (1, n):
    b[i] = b[i-1] + int(a[i])

i = 0
j = 0
ans = 0
while(i < n):
    sum = b[j] - b[i] + int(a[i])
    print(sum)
    if (sum <= t and ans < (j - i + 1)):
        ans = j - i + 1
    if (sum < t):
        j = j + 1
        if (j == n):
            break
    elif (sum >= t):
        i = i + 1
        if (i > j):
            j = i

print(ans)
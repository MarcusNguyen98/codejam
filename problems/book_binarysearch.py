n, t = input().split()
a = input().split()
t = int(t)
n = int(n)

b = [0 for i in range(n)]
b[0] = int(a[0])

for i in range (1, n):
    b[i] = b[i-1] + int(a[i])

def binary_search(index, low, high):
    ret = -1
    while(low <= high):
        mid = (low + high) // 2
        curT = b[mid] - b[index] + int(a[index])

        if (curT == t):
            return mid
        elif (curT < t):
            ret = mid
            low = mid + 1
        else:
            high = mid - 1

    return ret

ans = 0

for i in range(0, n):
    j = binary_search(i, i, n - 1)

    if (ans < (j - i + 1)):
        ans = j - i + 1

print(ans)

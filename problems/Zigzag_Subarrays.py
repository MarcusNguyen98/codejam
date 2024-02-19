import sys
input = sys.stdin.readline

T = int(input().strip())


sumArr = [0, 1]
for i in range(2, 100010):
    sumArr.append(sumArr[-1] + i)

def cal(start, end):
    length = end - start + 1
    if (length <= 1):
        return 0
    return length * (length - 1) - sumArr[length-1]

for _ in range(T):
    n = int(input().strip())
    A = [int(i) for i in input().strip().split()]

    if (n == 1):
        print(0)
        continue

    ans = 0
    start = 0
    end = -1
    for i in range(1, n):
        if (i - start >= 2):
            if (A[i] > A[i-1] and A[i-1] < A[i-2]):
                end = i
            elif (A[i] < A[i-1] and A[i-1] > A[i-2]):
                end = i
            else:
                # print('start ' + str(start) + ' end ' + str(end))
                ans += cal(start, end)
                start = end
                if (A[i] != A[i-1]):
                    end = i
                else:
                    start = i
        else:
            # print(i)
            if (A[i] != A[i-1]):
                end = i
                continue
            else:
                start = i

    # print('start ' + str(start) + ' end ' + str(end))
    if (start < end):
        ans += cal(start, end)
    # print('----------')
    print(ans)
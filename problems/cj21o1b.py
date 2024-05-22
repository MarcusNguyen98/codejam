import sys
input = sys.stdin.readline

T = int(input().strip())

while T > 0:
    T -= 1

    str = input().strip()
    arr = []

    for c in str:
        if c == '6':
            arr.append(9)
        else:
            arr.append(int(c))
    
    arr = sorted(arr, reverse=True)

    ele1 = arr[0]
    ele2 = arr[1]
    for idx in range(2, len(arr)):
        tmp1 = ele1 * 10 + arr[idx]
        tmp2 = ele2 * 10 + arr[idx]

        if (tmp1*ele2 < tmp2*ele1):
            ele2 = tmp2
        else:
            ele1 = tmp1

    print(ele1*ele2)
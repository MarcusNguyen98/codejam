import sys
input = sys.stdin.readline

N = int(input())
K = []
for i in range(N):
    K.append(int(input()))

def get(k):
    l = 1
    s = 0
    while (s + 3*(10**(l-1)*l) < k):
        s = s + 3*(10**(l-1)*l)
        l += 1
    
    y = 0
    if ((k-s) % l > 0):
        y = 10**(l-1) + 2 + ((k-s) // l)*3
    else:
        y = 10**(l-1) + 2 + ((k-s) // l - 1)*3
    indexOfY = (k-s) % l - 1
    if (indexOfY < 0):
        indexOfY = l - 1

    return int(str(y)[indexOfY])


def main():
    for i in range(N):
        ans = get(K[i]) + get(K[i] + 1) + get(K[i] + 2)
        print(ans)

main()
import sys
input = sys.stdin.readline

T = int(input().strip())

def cov(x):
    ret = ""
    for i in range(0, len(x)):
        c = x[i]
        if (c == '-'):
            c = chr(ord(' ') + 54 + 1)
        elif (c != ' '):
            isUpper = ord(c) >= ord('A') and ord(c) <= ord('Z')
            c = chr(ord(' ') + ((ord(c) - ord('A')) * 2 if isUpper else (ord(c) - ord('a')) * 2 + 1))
        ret += c

    return ret

for _ in range(T):
    n = int(input().strip())
    data = [["", ""] for _ in range(n)]
    for i in range(n):
        s = input().strip()
        data[i][0] = cov(s)
        data[i][1] = s

    data.sort(key=lambda x: x[0])

    for d in data:
        print(d[1])

# c = 'b'
# isUpper = ord(c) >= ord('A') and ord(c) <= ord('Z')
# print((ord(' ') + 1 + ((ord(c) - ord('A')) * 2 if isUpper else (ord(c) - ord('a')) * 2 + 1)))
# print(ord('A'))
# print(sorted(['aA', 'AA', 'AABcd', 'AaBcd']))
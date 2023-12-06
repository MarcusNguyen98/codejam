import sys
input = sys.stdin.readline

N = int(input())

# Python: To check if the string inp is a substring of the string S
def isSubstring(inp):
    size = len(inp)
    for i in range(size):
        if inp[i] != 'a' and inp[i] != 'b' and inp[i] != 'c': return False
    for i in range(size-1):
        if inp[i] == 'a' and inp[i+1] != 'b': return False
        if inp[i] == 'b' and inp[i+1] != 'c': return False
        if inp[i] == 'c' and inp[i+1] != 'a': return False
    return True
arr = []
for i in range(N):
    arr.append(input().replace('\n', ''))

for i in arr:
    if (isSubstring(i)):
        print('YES')
    else:
        print('NO')



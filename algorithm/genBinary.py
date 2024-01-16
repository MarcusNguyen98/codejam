N = 5
x = [0 for i in range(N)]
def genBinary(idx):
    if (idx == N):
        print(*x)
        return
    for i in range(2):
        x[idx] = i
        genBinary(idx+1)

genBinary(0)

    
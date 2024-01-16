import sys
input = sys.stdin.readline

MOD = 10**9 + 7

T = int(input())

def powMod(x, y):
    res = 1
    x = x % MOD
    while (y > 0):
        if y & 1:
            res = res*x
        y = y//2
        x = (x*x) % MOD
    return res

giaithua = [1 for _ in range(2 * (10 ** 5) + 1)]
powarr = [1 for _ in range(2 * (10 ** 5) + 1)]
for i in range(2, 2 * (10 ** 5) + 1):
    giaithua[i] = (i * giaithua[i-1]) % MOD
    powarr[i] = (powarr[i-1] * powMod(i, MOD - 2)) % MOD
# A1 = [N, M-1] => B1 = 2*N - 1 - A1
# B2 = M - B1 => A2 = M - 1 - A1
# Ckn = n! / (n - k)!*k!
# C(n-1) (n + k  -1) = (n-1)! / (k)! * (n-1)!
def tohoplap(k, n):
    # (A / B) % p = (A * B^(p-2)) % p = ((A % p) * (B^(p-2) % p)) % p
    A = giaithua[n] % MOD
    B = ((giaithua[n - k] % MOD ) * (giaithua[k] % MOD)) % MOD 
    powModOfB = powarr[n-k] * powarr[k]
    return ((A % MOD) * (powModOfB % MOD)) % MOD



ans = []
for _ in range(T):
    N, M = [int(i) for i in input().split()]

    res = 0
    for i in range(N, M):
        A1 = i
        B1 = 2 * N - 1 - A1
        A2 = M - 1 - A1
        B2 = M - B1
        if (B1 < 0):
            break
        res = (res + tohoplap(A1, B1+A1) * tohoplap(A2 , B2+A2) % MOD) % MOD
    
    ans.append(res)

for i in ans:
    print(i)


# MOD = 10 ** 9 + 7
 
# fact = [1 for _ in range(2 * (10 ** 5) + 1)]
# invv = [1 for _ in range(2 * (10 ** 5) + 1)]
 
 
# def init():
#     for i in range(2, 2 * (10 ** 5) + 1):
#         fact[i] = (fact[i - 1] * i) % MOD
#     for i in range(2, 2 * (10 ** 5) + 1):
#         invv[i] = (invv[i - 1] * inv(i, MOD)) % MOD
 
 
# def comb(n, k):
#     return ((fact[n] * invv[k]) % MOD * invv[n - k]) % MOD
 
 
# def inv(x, mod):
#     return pow(x, mod - 2, mod)
 
 
# def solve(case):
#     n, m = map(int, sys.stdin.readline().split())
 
#     res = 0
#     for i in range(n):
#         res = (res + comb(n - 1 + i, i) * comb(m - i - 1 + (m - n), m - i)) % MOD
 
#     print(res)
 
 
# if __name__ == "__main__":
#     init()
#     # t = 1
#     t = int(sys.stdin.readline())
#     for i in range(t):
#         solve(i)
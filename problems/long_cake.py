import sys
input = sys.stdin.readline

MOD = 10**9 + 7
TC = int(input().strip())

MAX = 1000000
fact = [1]
for i in range(1, MAX+1):
    fact.append((fact[-1] * i) % MOD)

def modexp(a, k, m):
    if m == 1:
        return 0
    if a == 1:
        return 1
 
    ret = 1
    base = a
    while k:
        if k & 1:
            ret *= base
            ret %= m
 
        k >>= 1
        base *= base
        base %= m
 
    return ret

ans = []
while(TC > 0):
    TC -= 1

    n, k = [int(i) for i in input().split()]
    A = list(input().strip())

    if (k == 1):
        ans.append(1)
        continue

    total = 0
    for i in range(n):
        if (A[i] == '1'):
            total += 1

    if (total == 0):
        n -= 1
        k -= 1
        #Ckn = n! / (n - k)!*k!
        # (A / B) % p = (A * B^(p-2)) % p = ((A % p) * (B^(p-2) % p)) % p
        
        ans.append((fact[n] * modexp((fact[n-k]*fact[k]) % MOD, MOD - 2, MOD) % MOD ) % MOD)
        continue
    
    if (total % k != 0):
        ans.append(0)
        continue
    
    cur_ans = 1
    lo, hi = 0, 0
    each = total // k
    picked = 0
    while(picked < k):
        cur = 0
        while(lo < n and cur < each):
            if (A[lo] == '1'):
                cur += 1
            lo += 1
        
        lo -= 1
        hi = lo + 1
        while(hi < n and A[hi] == '0'):
            hi += 1
        
        picked += 1
        if hi < n:
            cur_ans = (cur_ans * (hi - lo)) % MOD

        lo = hi

    ans.append(cur_ans)



for i in ans:
    print(i)
import sys
input = sys.stdin.readline

bills = [int(i) for i in input().split()]
moneys = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000]
total = int(input())

ans = 0
tmp = 0
cur = 0
for i in range(9):
    tmp += bills[i] * moneys[i]
    ans += bills[i]
    cur = i
    if (tmp >= total):
        break

if (tmp > total):
    while(cur >= 0):
        cnt = 1
        while(cnt <= bills[cur]):
            tmp -= moneys[cur]
            cnt += 1
            ans -= 1

            if (tmp == total):
                break
            if (tmp < total):
                tmp += moneys[cur]
                ans += 1
                break
        cur -= 1
        if (tmp == total):
            break

print(ans)

import sys
input = sys.stdin.readline

N = int(input())
temp = input().split()
arr = [int(temp[i]) for i in range(N)]
arr = sorted(arr)
pq = input().split()

arr2 = [0 for i in range(N+1)]
for i in range(N-1):
	arr2[i] = (arr[i+1] + arr[i]) // 2

arr2[N-1] = int(pq[0])
arr2[N] = int(pq[1])
arr2 = sorted(arr2)

ans = 0
max = 0
for i in range(N+1):
	if (arr2[i] > int(pq[1])):
		break
	kcnn = 99999999999999
	for j in range(N):
		kcnn = min(kcnn, abs(arr[j] - arr2[i]))
	
	if max < kcnn:
		max = kcnn
		ans = arr2[i]
print(ans)

import sys
input = sys.stdin.readline

N = int(input())
A = [int(i) for i in input().split()]

st = []
ans = 0

for i in range(N):
    if (len(st) == 0):
        st.append(A[i])
    else:
        tail = st[-1]
        if (tail >= A[i]):
            ans += 1
            if (tail != A[i]):
                st.append(A[i])
        else:
            ans += 1
            while(tail < A[i]):
                st.pop()
                if (len(st) > 0):
                    ans += 1
                    tail = st[-1]
                else:
                    break
            if (len(st) == 0 or st[-1] != A[i]):
                st.append(A[i])

print(ans)

# stack = []
# def main():
#     res  = n - 1
#     stack.append(arr[0])
#     for i in range(1, n):
#         if stack:
#             if arr[i] >= stack[0]:
#                 res += len(stack) - 1
#                 stack.clear()
#             else:
#                 element = stack[-1]
#                 while stack:
#                     if element < arr[i]:
#                         stack.pop(-1)
#                         element = stack[-1]
#                         res += 1
#                     else:
#                         break
#         stack.append(arr[i])
#     print(res)
# main()

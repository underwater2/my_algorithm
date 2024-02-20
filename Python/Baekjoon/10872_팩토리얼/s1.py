import sys

N = int(sys.stdin.readline())
ans = 1

for i in range(N, 1, -1):
    ans *= i
print(ans)

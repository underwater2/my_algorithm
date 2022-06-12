# dfs?
# 안풀림

import sys
sys.stdin = open('input.txt')

def dfs(now):
    global amount, maxA
    # if now >= 7:
    #     maxA = max(amount, maxA)
    #     return
    for n in range(now, N+1):
        if n == N:
            maxA = max(amount, maxA)
            return
        if (n + tp[n][0]) <= N:
            amount += tp[n][1]
            dfs(now + tp[n][0])
            amount -= tp[n][1]


N = int(sys.stdin.readline())

tp = [0]
for _ in range(N):
    tp.append(list(map(int, sys.stdin.readline().split())))

now = 1 # 현재위치
amount = 0
maxA = 0
# visited = [0] * (N+1)
dfs(3)
print(maxA)

print(tp)
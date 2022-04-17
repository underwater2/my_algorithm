# bfs

import sys
sys.stdin = open('input.txt')

from collections import deque

# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(M)]
que = deque()

for n in range(N):
    for m in range(M):
        if tomato[m][n] == 1:
            que.appendleft((m, n, 0))
result = 0
while que:
    i, j, day = que.pop()  # i가 행, j가 열, day는 현재 상태까지 지난 날짜
    for t in range(4):
        ni = i + di[t]
        nj = j + dj[t]
        if 0 <= ni < M and 0 <= nj < N:
            if tomato[ni][nj] == 0:
                tomato[ni][nj] = 1
                que.appendleft((ni, nj, day+1))
                result = day+1

for n in range(N):
    for m in range(M):
        if tomato[m][n] == 0:
            result = -1

print(result)
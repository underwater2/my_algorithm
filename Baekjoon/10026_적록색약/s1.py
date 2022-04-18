# bfs
# 일반일 때 구역수 구하기 -> R색을 G색으로 바꾸기 -> 적록색맹일 때 구역수 구하기
    # 이렇게 하면 시간초과 나지 않을까 했는데, 다들 이렇게 풀었더라.

import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(arr, visited):
    que = deque()
    que.appendleft((i, j))
    color = arr[i][j]
    while que:
        xi, xj = que.pop()
        for t in range(4):
            ni, nj = xi + di[t], xj + dj[t]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if arr[ni][nj] == color:
                    visited[ni][nj] = 1
                    que.appendleft((ni, nj))


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())
arr = [list(input()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

colorN = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:  # 이미 구분된 구역이 아닐 때
            # bfs
            bfs(arr, visited)
            colorN += 1


# 적록색약
    # 사전에 arr의 G 글자를 R로 바꿔버림
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

visited_rg = [[0] * N for _ in range(N)]

colorN_rg = 0
for i in range(N):
    for j in range(N):
        if visited_rg[i][j] == 0:  # 이미 구분된 구역이 아닐 때
            # bfs
            bfs(arr, visited_rg)
            colorN_rg += 1
print(colorN, colorN_rg)



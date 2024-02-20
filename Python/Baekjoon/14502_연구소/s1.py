# bfs
# 완전 탐색
    # N, M의 범위가 8까지 였던 게 힌트 아니었나 추측

import sys
sys.stdin = open('input.txt')

from itertools import combinations
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
blank = list()
que = deque()

# 0의 위치를 blank list에 담기
# 2의 위치를 queue에 담기
for n in range(N):
    for m in range(M):
        if arr[n][m] == 0:
            blank.append((n, m))
        if arr[n][m] == 2:
            que.appendleft((n,m))

maxN = -1
for i in combinations(blank, 3):
    result = 0
    # 받은 arr를 깊은 복사
    copy_arr = [item[:] for item in arr]
    # que를 복사 (검색했을 때 얕은 복사라는데, 해보면 깊은 복사 같다 ???)
    copy_que = que.copy()

    for j in i:
        copy_arr[j[0]][j[1]] = 1
    # bfs
    while copy_que:
        xi, xj = copy_que.pop()
        for t in range(4):
            ni, nj = xi + di[t], xj + dj[t]
            if 0 <= ni < N and 0 <= nj < M:
                if copy_arr[ni][nj] == 0:
                    copy_arr[ni][nj] = 2
                    copy_que.appendleft((ni, nj))

    for n in range(N):
        for m in range(M):
            if copy_arr[n][m] == 0:
                result += 1

    if result > maxN:
        maxN = result
print(maxN)
# input 대신 sys.stdin.readline() 쓰기
# width, height / 행, 열 조합이 또 헷갈렸다.

import sys
sys.stdin = open('input.txt')

from collections import deque

# 우하좌상, 대각선 4방향
di = [0, 1, 0, -1, -1, 1, -1, 1]
dj = [1, 0, -1, 0, -1, 1, 1, -1]

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]

    islandNum = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                # bfs
                queue = deque([(i, j)])
                while queue:
                    x, z = queue.pop()
                    maps[x][z] = 0
                    for t in range(8):
                        nx = x + di[t]
                        nz = z + dj[t]
                        if 0 <= nx < h and 0 <= nz < w:
                            if maps[nx][nz] == 1:
                                queue.appendleft((nx, nz))
                                maps[nx][nz] = 0
                islandNum += 1

    print(islandNum)




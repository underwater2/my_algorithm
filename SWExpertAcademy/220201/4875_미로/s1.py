# 함수를 이용한 DFS (재귀)
# https://velog.io/@jiffydev/algo-63

import sys
sys.stdin = open('sample_input.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(i, j):
    try:
        global flag
        if flag:
            return

        if maze[i][j] == 3:
            flag = 1

        for t in range(4):
            ni = i + di[t]
            nj = j + dj[t]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and maze[ni][nj] != 1:
                visited[ni][nj] = 1
                dfs(ni, nj)
                visited[ni][nj] = 0
    except:
        flag = 'error'


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 2 출발점 찾기
    flag = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                visited[i][j] = 1
                dfs(i, j)
    print('#{} {}'.format(tc, flag))
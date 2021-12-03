# dfs 재귀로 풀었는데 계속 시간초과가 나서 버렸다.
# 검색하니 파이썬이면 재귀는 못쓴다고 보면 된다는 말이 있었다.
di = [1, 0, -1, 0]  # 하우상좌
dj = [0, 1, 0, -1]

def dfs(arr, i, j):
    global cnt, maxV
    cnt += 1
    visited[i][j] = 1

    if cnt > maxV:
        return

    if i == N-1 and j == M-1:
        if maxV > cnt:
            maxV = cnt

    for t in range(4):
        ni = i + di[t]
        nj = j + dj[t]
        if 0 <= ni < N and 0 <= nj < M:
            if not visited[ni][nj] and maze[ni][nj] == 1:
                dfs(arr, ni, nj)
                visited[ni][nj] = 0
                cnt -= 1


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0
maxV = 987654321
dfs(maze, 0, 0)
print(maxV)
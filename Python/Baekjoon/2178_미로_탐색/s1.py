# bfs
# 최단거리 문제는 최단거리를 보장하는 bfs를 사용해야한다.
# dfs는 최단거리를 찾으려면 완전 탐색을 하고 그 중에서 가장 작은값을 선택해야 한다. 경로가 많을수록 시간 복잡도가 매우 커진다.

# 이미 왔던 곳을 중복해서 가면 안된다. 그래서 visited 배열을 사용.
# 항상 최단거리를 보장하므로 visited 값이 큰지 작은지 고려할 필요가 없다.

# 잘 설명한 링크
# https://wonit.tistory.com/421?category=750230


from collections import deque

di = [0, 1, 0, -1]  # 우하좌상
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def bfs():
    queue = deque()
    queue.appendleft((0, 0))
    visited[0][0] = 1

    while queue:
        i, j = queue.pop()
        if (i, j) == (N-1, M-1):
            return visited[i][j]
        for t in range(4):
            ni = i + di[t]
            nj = j + dj[t]
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] and not visited[ni][nj]:
                queue.appendleft((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

print(bfs())


# dfs 재귀로 풀었는데 계속 시간초과가 나서 버렸다.
# 검색하니 파이썬이면 재귀는 못쓴다고 보면 된다는 말이 있었다.
# di = [1, 0, -1, 0]  # 하우상좌
# dj = [0, 1, 0, -1]
#
# def dfs(arr, i, j):
#     global cnt, maxV
#     cnt += 1
#     visited[i][j] = 1
#
#     if cnt > maxV:
#         return
#
#     if i == N-1 and j == M-1:
#         if maxV > cnt:
#             maxV = cnt
#
#     for t in range(4):
#         ni = i + di[t]
#         nj = j + dj[t]
#         if 0 <= ni < N and 0 <= nj < M:
#             if not visited[ni][nj] and maze[ni][nj] == 1:
#                 dfs(arr, ni, nj)
#                 visited[ni][nj] = 0
#                 cnt -= 1
#
#
# N, M = map(int, input().split())
# maze = [list(map(int, input())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
# cnt = 0
# maxV = 987654321
# dfs(maze, 0, 0)
# print(maxV)
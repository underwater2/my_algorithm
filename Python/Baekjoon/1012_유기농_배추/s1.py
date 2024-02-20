# bfs

# deque를 넣었다 뺐다 해서 시간초과 날 줄 알았는데, 통과
# M과 N이 헷갈렸다

from collections import deque

di = [0, 1, 0, -1]  # 우하좌상
dj = [1, 0, -1, 0]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited = deque()

    while queue:
        x, y = queue.pop()
        visited.append((x, y))
        for t in range(4):
            nx = x + di[t]
            ny = y + dj[t]
            if 0 <= nx < M and 0 <= ny < N:
                if (nx, ny) in edge and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    edge.remove((nx, ny))


T = int(input())

for _ in range(1, T+1):
    M, N, K = map(int, input().split())  # N: 세로길이, M: 가로길이
    edge = deque()
    for _ in range(K):
        i, j = map(int, input().split())
        edge.append((i, j))

    cnt = 0
    while edge:
        x, y = edge.pop()
        bfs(x, y)
        cnt += 1

    print(cnt)
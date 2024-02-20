# bfs
# dfs보다 빠를 것 같아서 bfs로 풀었다.
# 1을 찾기 위해 arr를 쭉 완전탐색 해야하기 때문에 시간초과가 날 것 같았는데, 괜찮았다.

from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j):
    queue = deque()
    queue.appendleft((i, j))
    cnt = 0
    while queue:
        i, j = queue.pop()
        house[i][j] = 0
        visited[i][j] = 1
        cnt += 1
        for t in range(4):
            ni = i + di[t]
            nj = j + dj[t]
            if 0 <= ni < N and 0 <= nj < N and house[ni][nj] and not visited[ni][nj] and (ni, nj) not in queue:
                queue.appendleft((ni, nj))
    return cnt


N = int(input())
house = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
houses = deque()  # 단지 내 집의 수 배열로 저장

for i in range(N):
    for j in range(N):
        if house[i][j]:
            houses.append(bfs(i, j))

houses = sorted(houses)
complexes = len(houses)
print(complexes)
for i in range(complexes):
    print(houses[i])
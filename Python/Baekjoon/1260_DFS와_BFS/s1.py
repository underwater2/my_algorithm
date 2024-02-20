# dfs, bfs
# dfs를 잘못해서 틀렸었다.

# deque 사용
# stack 메서드 - append(), pop()
# queue 메서드 - appendleft(), pop()

from collections import deque

def dfs(start):
    visited_dfs[start] = 1
    dfs_ans.append(start)
    for i in range(1, N+1):
        if not visited_dfs[i] and arr[start][i] == 1:
            dfs(i)


def bfs():
    dq = deque()
    dq.appendleft(V)
    while dq:
        el = dq.pop()
        visited_bfs[el] = 1
        bfs_ans.append(el)
        for i in range(1, N+1):
            if arr[el][i] == 1 and visited_bfs[i] == 0 and i not in dq:
                dq.appendleft(i)


N, M, V = map(int, input().split())
# 2차원 배열로 간선 나타냄
arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

visited_dfs = [0 for _ in range(N+1)]
dfs_ans = []
dfs(V)
print(*dfs_ans)


visited_bfs = [0 for _ in range(N+1)]
bfs_ans = []
bfs()
print(*bfs_ans)
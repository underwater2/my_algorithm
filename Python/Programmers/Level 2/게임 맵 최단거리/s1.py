# 최단거리 => BFS

from collections import deque

di = [0, 1, 0, -1]  # 우하좌상
dj = [1, 0, -1, 0]

def solution(maps):
    n, m = len(maps[0]), len(maps)
    queue = deque([(0,0,1)])  # (i,j,지나온 칸 개수)
    maps[0][0] = 0
    while queue:
        i, j, cnt = queue.popleft()
        for t in range(4):
            ni = i+di[t]
            nj = j+dj[t]
            if 0 <= ni < m and 0 <= nj < n and maps[ni][nj]:  # 아직 지나지 않은 칸이면
                if (ni, nj) == (m-1, n-1):  # 상대 진영에 도달했을 때
                    return cnt+1
                maps[ni][nj] = 0  # 같은 좌표가 queue에 또 들어가지 않도록 0으로 바꿈
                queue.append((ni, nj, cnt+1))
    return -1  # 상대 진영에 도달하지 못하면 반환
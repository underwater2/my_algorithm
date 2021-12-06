# bfs
# 시간초과 떠서 헤매다가, 다른 사람 코드 처럼 visited를 배열의 인덱스를 숫자로 해서 0, 1로 표시했다.
# 처음에 deque로 했을 때는 계속 append 해야하고,
# ni not in visited 로 ni를 서치해야하기 때문에 시간초과가 났던 것 같다.

from collections import deque

N, K = map(int, input().split())
# visited = deque()
visited = [0] * 100001

def bfs():
    if N == K:
        return 0
    queue = deque()
    queue.appendleft(N)
    visited[N] = 0
    while queue:
        i = queue.pop()
        for ni in [i-1, i+1, i*2]:
            if 0 <= ni < 100001 and not visited[ni]:
                queue.appendleft(ni)
                visited[ni] = visited[i] + 1
                if ni == K:
                    return visited[ni]

print(bfs())
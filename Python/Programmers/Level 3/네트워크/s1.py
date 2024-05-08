from collections import deque

def solution(n, computers):
  ncount = 0
  visited = [0] * n
  q = deque()
  for i in range(0, n):
    if visited[i] == 0:
      q.append(i)
      visited[i] = 1
      ncount += 1
    # BFS
    while q:
      now = q.popleft()
      for t in range(0, n):
        if visited[t] == 0 and computers[now][t] == 1:
          q.append(t)
          visited[t] = 1

  return ncount
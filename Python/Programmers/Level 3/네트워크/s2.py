def dfs(i, n, visited, computers):
  visited[i] = 1
  for t in range(0, n):
    if visited[t] == 0 and computers[i][t] == 1:
      dfs(t, n, visited, computers)


def solution(n, computers):
  ncount = 0
  visited = [0] * n
  for i in range(0, n):
    if visited[i] == 0:
      # DFS
      dfs(i, n, visited, computers)
      ncount += 1

  return ncount
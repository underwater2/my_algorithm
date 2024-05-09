def dfs(depth, n, path, used, tickets, paths):
  depth += 1

  if depth == n:
    paths.append(path[:])
    return

  for t in range(0, n):
    if used[t] == 0 and path[-1] == tickets[t][0]:
      used[t] = 1
      path.append(tickets[t][1])
      dfs(depth, n, path, used, tickets, paths)
      used[t] = 0
      path.pop()


def solution(tickets):
  n = len(tickets)
  paths = []

  for i in range(n):
    if tickets[i][0] == "ICN":
      path = tickets[i]
      used = [0 for _ in range(n)]
      used[i] = 1
      dfs(0, n, path, used, tickets, paths)

  return sorted(paths)[0]
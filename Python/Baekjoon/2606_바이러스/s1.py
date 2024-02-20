import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(input())
M = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

que = deque()
visited = [0] * (N+1)
que.appendleft(1)
visited[1] = 1
while que:
    x = que.pop()
    for i in range(1, N+1):
        if arr[x][i] and not visited[i]:
            que.appendleft(i)
            visited[i] = 1
print(sum(visited)-1)
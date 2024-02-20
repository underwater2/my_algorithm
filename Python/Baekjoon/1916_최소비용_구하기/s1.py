import sys
sys.stdin = open('input.txt')

import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
bus = [[] for _ in range(N+1)]
for i in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    bus[s].append((e, c))
start_city, end_city = map(int, sys.stdin.readline().split())

distance = [987654321] * (N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start_city))
    distance[start_city] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        else:
            for i in bus[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
dijkstra(start_city)
print(distance[end_city])

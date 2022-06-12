# 다익스트라 알고리즘으로만 풀 수 있다
# https://jaemunbro.medium.com/algorithm-%EC%B5%9C%EB%8B%A8-%EA%B2%BD%EB%A1%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-with-python-20f061fdc8f1
# 위 사이트의 코드 참고

import sys
sys.stdin = open('input.txt')

import heapq

V, E = map(int, sys.stdin.readline().split())  # V: 정점 개수 , E: 간선 개수
K = int(sys.stdin.readline())  # K: 시작 정점의 번호
# 2차원 배열 (행 -> 열 간선)
edge = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edge[u].append((v, w))

distance = [987654321] * (V+1)  # start 점으로부터 idx 까지의 최소거리

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        else:
            for i in edge[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == 987654321:
        print('INF')
    else:
        print(distance[i])


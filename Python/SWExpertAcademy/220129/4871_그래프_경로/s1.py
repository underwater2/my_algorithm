# 스택칸에 있는 문제
# 반복문으로 풂. 재귀는 시간초과 때문에 안함
# PASS했으나 코드 리뷰 필요

import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def dfs(start, end, edge):  # 출발노드, 도착노드, 연결리스트
    stack = deque()
    global visited
    v = start
    visited[v] = 1
    stack.append(v)  # 노드에 도착하는 즉시 stack에 저장
    while stack:
        for i in edge[v]:
            if not visited[i]:
                if i == end:  # 도착노드 찾으면 함수 끝냄
                    return 1
                v = i
                stack.append(v)
                visited[v] = 1
                break  # for문 끝내고 다시 while문 시작으로
        else:
            v = stack.pop()  # 갈 수 있는 노드가 없으면 바로 직전 노드로 돌아감
    return 0  # 끝까지 돌았는데 도착노드를 못찾음


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())  # V노드, E간선
    edge = list([] for _ in range(V+1))  # 연결리스트
    for _ in range(E):
        a, b = map(int, input().split())
        edge[a].append(b)  # 방향성 그래프. 인덱스가 출발점, value가 도착점
    S, G = map(int, input().split())  # S출발노드, G도착노드
    visited = [0 for _ in range(V + 1)]  # 방문했던 노드 저장
    print('#{} {}'.format(tc, dfs(S, G, edge)))


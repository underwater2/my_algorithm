# heapq 사용 코드

import sys
sys.stdin = open('input.txt')

import heapq

N = int(sys.stdin.readline())
q = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(q, -x)
    else:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)

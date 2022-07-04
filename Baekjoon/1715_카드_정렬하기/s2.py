# 우선순위 큐 사용해야함
    # https://www.acmicpc.net/board/view/89944
    # 우선순위 큐에서 매 차례 가장 작은 수의 묶음을 선택해야 한다.

# PriorityQueue보다는 heapq를 사용하여 우선순위큐 문제를 해결하는 게 좋다.
    # PriorityQueue 사용하면 시간초과 문제가 발생하는 경우가 있었다.

import sys
sys.stdin = open('input.txt')

import heapq

N = int(sys.stdin.readline().rstrip())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline().rstrip()))
ans = 0
while len(cards) != 1:
    A = heapq.heappop(cards)
    B = heapq.heappop(cards)
    AB = A + B
    ans += AB
    heapq.heappush(cards, AB)
print(ans)

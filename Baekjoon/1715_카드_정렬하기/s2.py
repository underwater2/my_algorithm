# 우선순위 큐 사용해야함
    # https://www.acmicpc.net/board/view/89944
    # 우선순위 큐에서 매 차례 가장 작은 수의 묶음을 선택해야 한다.

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

import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(sys.stdin.readline())
cards = deque([i for i in range(1, N+1)])

while len(cards) != 1:
    cards.popleft()
    # cards.append(cards.popleft())
    cards.rotate(-1)
print(*cards)
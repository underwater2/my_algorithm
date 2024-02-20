import sys
sys.stdin = open('input.txt')

from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

data = combinations(cards, 3)

maxN = 0
for i in data:
    sumV = sum(i)
    if sumV > maxN and sumV <= M:
        maxN = sumV

print(maxN)
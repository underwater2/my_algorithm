import sys
sys.stdin = open('input.txt')

from itertools import combinations

dwarf = [int(sys.stdin.readline()) for _ in range(9)]

data = combinations(dwarf, 7)

for i in data:
    if sum(i) == 100:
        for height in sorted(list(i)):
            print(height)
        break
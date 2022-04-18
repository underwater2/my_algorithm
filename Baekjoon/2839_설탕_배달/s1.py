# Greedy

import sys
sys.stdin = open('input.txt')

N = int(input())

A = N//5
result = -1
for a in range(A, -1, -1):
    M = N - 5*a
    if not M % 3:
        result = a + M//3
        break
    else:
        continue
print(result)
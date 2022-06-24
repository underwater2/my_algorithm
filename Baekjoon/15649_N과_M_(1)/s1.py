#  백트래킹 (DFS) 분류의 문제였지만, 순열로 풀었다...

import sys
sys.stdin = open('input.txt')

from itertools import permutations

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

for perm in permutations(arr, M):
    print(*perm)
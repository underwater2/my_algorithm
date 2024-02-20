import sys
sys.stdin = open('input.txt')

from collections import deque

N, K = map(int, sys.stdin.readline().split())
arr = deque([i for i in range(1, N+1)])
perm = deque()

while arr:
    arr.rotate(-K+1)
    perm.append(str(arr.popleft()))
print('<' + ', '.join(perm) + '>')
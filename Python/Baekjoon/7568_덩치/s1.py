import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
rank = [1 for _ in range(N)]
wh = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(0, N-1):
    for j in range(i+1, N):
        if wh[i][0] > wh[j][0] and wh[i][1] > wh[j][1]:
            rank[j] += 1
        elif wh[i][0] < wh[j][0] and wh[i][1] < wh[j][1]:
            rank[i] += 1

print(*rank)
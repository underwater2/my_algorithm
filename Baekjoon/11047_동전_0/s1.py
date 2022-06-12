# Greedy
# 아래처럼 bisect를 쓰면 문제가 틀린다.
# K_idx = bisect.bisect_left(coin, K)

import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]
cnt_coin = 0

for i in range(N-1, -1, -1):

    if K >= coin[i]:
        cnt_coin += K // coin[i]
        K %= coin[i]

    if K == 0:
        print(cnt_coin)
        break


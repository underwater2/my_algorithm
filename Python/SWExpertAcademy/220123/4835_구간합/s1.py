import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    max_num = -1
    min_num = 987654321

    for i in range(0, N-M+1):
        total = 0
        for j in range(0, M):
            total += ai[i+j]
        if total > max_num:
            max_num = total
        if total < min_num:
            min_num = total
    print('#{} {}'.format(tc, max_num - min_num))
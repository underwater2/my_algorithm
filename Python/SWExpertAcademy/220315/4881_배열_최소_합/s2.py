# dfs 백트래킹
# 블로그에서 따라친 코드 : https://glory-summer.tistory.com/82
import sys
sys.stdin = open('sample_input.txt')

def section_sum(idx, total):
    global answer

    if idx == N:
        if total < answer:
            answer = total
            return

    if total > answer:
        return

    for i in range(N):
        if i not in visited:
            visited.append(i)
            section_sum(idx+1, total + matrix[idx][i])
            visited.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 10*10  # 큰 값
    visited = []
    section_sum(0, 0)
    print('#{} {}'.format(tc, answer))
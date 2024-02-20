# memoization, DP 관련 문제
# 위의 개념 영상과 풀이를 보고 풀었다

# deque 사용법
# https://velog.io/@gillog/Python-Stack-Queue-%EA%B8%B0%EB%B3%B8-module-%EC%82%AC%EC%9A%A9-%EC%A0%95%EB%A6%AC

# 그림 보고 규칙 찾아서 푼 답변
# https://j-ungry.tistory.com/149

# 등비수열 규칙 찾아서 푼 답변
# https://totoma3.tistory.com/126

# 점화식
# f(n) = f(n-1) + 2f(n-2)

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) // 10
    memo = [0, 1, 3]  # 인덱스는 N // 10
    if N >= 3:
        for i in range(3, N+1):
            if len(memo) < i+1:
                memo.append(memo[i-1] + 2 * memo[i-2])
    print('#{} {}'.format(tc, memo[N]))

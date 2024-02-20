# dp 문제
    # 조건을 잘못봐 정수 2, 3의 경우를 잘못 구해서 계속 삽질했다.
    # 참고 블로그
        # https://jyami.tistory.com/15
        # https://this-programmer.tistory.com/96

import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().rstrip())

for _ in range(1, T+1):
    n = int(sys.stdin.readline().rstrip())
    dp = [0] * 12
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])

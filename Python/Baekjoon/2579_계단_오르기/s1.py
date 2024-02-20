# dp
# 전 계단 제외 최댓값 = 전전 계단의 진최댓값 + 현재 계단의 점수
# 위 식에서 필요한 '진최댓값'과 '전 계단 제외 최댓값' 변수로 하여, 앞에서부터 구해가며 저장했다.
    # 다른 풀이를 보니, 위 식을 이용해서 진최댓값만 저장할 수도 있었다.

import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())

stair = [0] + [int(sys.stdin.readline().rstrip()) for _ in range(N)]

dp = [0 for _ in range(N+1)] # 진최댓값
exdp = [0 for _ in range(N+1)] # 전 계단 제외 최댓값

dp[1] = stair[1]
exdp[1] = stair[1]

if N > 1:
    dp[2] = stair[1] + stair[2]
    exdp[2] = stair[2]

    for i in range(3, N+1):
        exdp[i] = dp[i-2]+stair[i]
        dp[i] = max(stair[i]+exdp[i-1], stair[i]+dp[i-2])

print(dp[N])

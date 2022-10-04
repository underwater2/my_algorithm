# dp 문제
# 아래 해설 보고 풀었다.
    # https://school.programmers.co.kr/questions/21365

def solution(land):
    dp = [[0]*4 for _ in range(len(land))]
    dp[0] = land[0]
    for i in range(1, len(land)):
        for j in range(4):
            maxN = 0
            for k in range(4):
                if k == j:
                    continue
                else:
                    maxN = max(maxN, dp[i-1][k])
            dp[i][j] = maxN + land[i][j]
    return max(dp[-1])
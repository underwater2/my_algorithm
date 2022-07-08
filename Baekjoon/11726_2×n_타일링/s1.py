# dp

import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().rstrip())

dp = [0] * 1001
dp[1], dp[2] = 1, 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])
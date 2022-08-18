# dp 문제
# 시간초과 문제가 있었음
    # 1. 함수 밖에 dp를 선언하고 필요한 만큼만 append 진행했더니 드는 시간이 줄었지만 마지막 tc 시간초과.
        # => 한 번 run 하는 동안 테스트 케이스 모두를 테스트 하는듯
    # 2. dp에 값을 저장하기 전에 매번 % 1000000007 연산한다.
        # => 이렇게 해도 답은 동일하다.
        # => 피보나치 수열을 구하는 경우, 숫자가 커질 수록 시간이 더 많이 걸린다.
    # *. 리스트를 사용하지 않고 변수만을 이용해서 푼다.
        # => s2.py에 정리

dp = [0, 1, 2]

def solution(n):
    for i in range(len(dp), n+1):
        dp.append((dp[i-1] + dp[i-2]) % 1000000007)
    return dp[n]
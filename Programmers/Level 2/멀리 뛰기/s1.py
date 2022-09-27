# DP
# 조합 식(math.factorial 사용) 풀었다가 숫자 크기 에러 나서 DP로 바꿨다.

def solution(n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(n-2):
        a, b = b % 1234567, (a+b) % 1234567
    return b
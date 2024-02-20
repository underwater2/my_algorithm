def solution(n):
    ans = 0
    while n:
        if n % 2:  # 홀수일 때
            n -= 1
            ans += 1
        else:
            n //= 2
    return ans
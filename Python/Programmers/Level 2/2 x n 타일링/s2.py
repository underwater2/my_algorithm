def solution(n):
    a, b = 0, 1
    for i in range(n):
        temp = b
        b += a
        a = temp
    return b % 1000000007
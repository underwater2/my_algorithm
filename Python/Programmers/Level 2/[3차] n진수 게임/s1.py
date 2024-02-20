# 숫자 하나씩 더해가면서 원하는 순서까지 만듦

# 어느 숫자까지 변환해야할지 고민됐다.
    # https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-n%EC%A7%84%EC%88%98-%EA%B2%8C%EC%9E%84-Python
    # 여기서는 m*t 까지 변환함.
    # 내 경우 최소 길이를 알아내고 while문으로 하나씩 더할 때 마다 길이를 검사함.


def trans(n, k):  # 숫자 n, k진법
    result = ''
    alphabet = list('ABCDEF')
    while n > 0:
        n, mod = divmod(n, k)
        if (mod-10) >= 0:
            result += alphabet[mod-10]
        else:
            result += str(mod)
    return result[::-1]

def solution(n, t, m, p):
    answer = ''
    game = '01'
    now = 2
    while len(game) < p+(t-1)*m:
        game += trans(now, n)
        now += 1
    for i in range(p-1, p+(t-1)*m, m):
        answer += game[i]
    return answer
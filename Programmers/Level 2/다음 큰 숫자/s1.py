def func(n, cnt):
    n += 1
    bn = bin(answer)[2:]
    cnt1 = bn.count('1')
    if cnt1 == cnt:
        return int(bn, 2)
    elif cnt1 > cnt:
        return func(n, cnt)
    else:
        continue


def solution(n):
    answer = 4
    print(bin(answer))
    return answer
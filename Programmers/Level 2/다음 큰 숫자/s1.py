def func(n, cnt):
    n += 1
    bn = bin(n)[2:]
    cnt1 = bn.count('1')
    if cnt1 == cnt:
        return n
    elif cnt1 > cnt:
        return func(n, cnt)
    else:
        num = cnt - cnt1
        newn = ''
        for i in range(len(bn) - 1, -1, -1):
            if num > 0 and bn[i] == '0':
                newn = '1' + newn
                num -= 1
            else:
                newn = bn[i] + newn
        return int('0b' + newn, 2)


def solution(n):
    answer = func(n, bin(n)[2:].count('1'))
    return answer
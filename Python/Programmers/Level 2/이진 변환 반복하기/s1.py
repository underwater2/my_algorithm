# 메모이제이션을 써봤다.

cnt1 = [(-1, -1)] * 150001
cnt1[1] = (0, 0)

def solution(s):
    firsts = s
    ans0 = 0
    ans1 = 0
    while s != '1':
        c = s.count('1')
        c0 = s.count('0')
        ans1 += c0
        if cnt1[c] != (-1,-1):
            ans0 += cnt1[c][0]
            ans1 += cnt1[c][1]
            break
        s = format(c, 'b')
        ans0 += 1
    cnt1[firsts.count('1')] = ans0
    answer = [ans0+1, ans1]
    return answer
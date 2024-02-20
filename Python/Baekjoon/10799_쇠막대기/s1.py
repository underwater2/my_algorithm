# 다른 풀이를 보니 stack에 '('를 넣고 빼는 식의 풀이가 많았다.
# 나는 cnt 변수에  '('의 갯수만 셌다.

import sys
sys.stdin = open('input.txt')

stick = sys.stdin.readline().rstrip()

idx = 0
cnt = 0
ans = 0
while idx < len(stick):
    elem = stick[idx]
    if elem == ')':
        cnt -= 1
        idx += 1

    elif elem == '(':
        if stick[idx+1] == ')':
            ans += cnt
            idx += 2
        else:
            ans += 1
            cnt += 1
            idx += 1

print(ans)
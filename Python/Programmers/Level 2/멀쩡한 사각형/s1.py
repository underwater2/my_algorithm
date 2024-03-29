# x축 1부터 이동하면서 못쓰는 네모 수(cnt) 세기
# 세가면서 그때그때 w, h의 최대공약수인지 검사
# 최대공약수를 찾으면 해답 = cnt * 넓이/최대공약수

# 로직은 맞으나 테스트케이스 6번이 오류나는 경우
    # 자료형의 오차, 제한 범위도 고려해줘야한다.
    # https://school.programmers.co.kr/questions/19918
        # 6번은 자료형이 가지는 오차로 인해 발생합니다.
        # 아래와 같이 먼저 곱하고 나누는 순서로 계산하는 경우 오차가 줄어 통과가 됩니다.
        # h*x/w

# 다른 풀이 보니 최대공약수(gcd) 최대공배수(lcm) 함수 많이 씀
    # import math
    # math.gcd(5, 10, 15)
    # math.lcm(11, 22, 66)

import math

def solution(w,h):
    if w == 1 or h == 1:
        return 0
    cnt = h - math.floor(h * (w-1) / w)
    x = w-1
    minW = w
    while True:
        top = h * x / w
        bottom = h * (x-1) / w
        cnt += math.ceil(top) - math.floor(bottom)
        if bottom % 1 == 0.0:
            minW = w-x+1
            break
        x -= 1
    answer = w*h - (cnt * w/minW)
    return answer
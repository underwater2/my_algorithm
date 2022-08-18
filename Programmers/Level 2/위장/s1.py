# 해시맵 만든 후 경우의 수 계산
# 각 종류 별로 (옷 개수 + 안입는 경우 1)를 모두 곱한다 -> 모두 안입는 경우 1을 빼면 정답
# 문제풀이 참고 글
    # https://school.programmers.co.kr/questions/15225

from collections import defaultdict

def solution(clothes):
    answer = 1
    dt = defaultdict(list)
    for c in clothes:
        dt[c[1]].append(c[0])  # 옷의 이름은 모두 다르므로 숫자로만 계산해도 된다.
    for d in dt:
        answer *= (len(dt[d])+1)
    return answer-1
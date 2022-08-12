# 출처: 프로그래머스 다른 사람의 풀이

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        # permutations에 들어있는 ('1', '7') 같은 perm들을 모두 join해줌 => 모두 int로 변환 => set에 넣어 중복 제거
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))  # 0, 1은 소수가 아니므로 제거
    for i in range(2, int(max(a) ** 0.5) + 1):  # 에라토스테네스의 체
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

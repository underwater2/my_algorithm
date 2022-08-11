# 다중집합의 합집합, 교집합
    # 일반 집합의 합집합, 교집합을 구하고 min(), max()를 사용해서 구할 수도 있다.

import math

def solution(str1, str2):
    set1 = make_set(str1)
    set2 = make_set(str2)

    # 교집합 구하기
    temp_1 = set1.copy()  # 반드시 set1 원본이 아닌 복사본을 사용해야 한다.
    cnt_inter = 0
    for s in set2:
        if s in temp_1:
            cnt_inter += 1
            temp_1.remove(s)

    # 합집합 구하기
    result_1 = set1.copy()  # 결과로 나올 합집합
    temp_1 = set1.copy()  # 점검해야할 교집합 원소 모음
    for s in set2:
        if s in temp_1:
            temp_1.remove(s)  # s가 교집합에 속할 경우, 교집합 목록에서 뺀다
        else:
            result_1.append(s)
    cnt_union = len(result_1)
    if cnt_union == 0:
        return 65536

    answer = math.trunc(cnt_inter * 65536 / cnt_union)
    return answer


def make_set(st):  # 문자열 -> 다중집합의 원소
    li = []
    st = st.upper()  # 전부 대문자로 변환
    for i in range(len(st) - 1):
        s = st[i:i + 2]
        if s.isalpha():
            li.append(s)
    return li
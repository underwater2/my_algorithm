# 참고 코드
# https://codlingual.tistory.com/161

# # set.isSubset()
# x = {"홈짱닷컴", "Homzzang.com", "코딩강의"}
# y = {"홈짱닷컴", "Homzzang.com", "코딩강의", "2012"}
# res = x.issubset(y)  # x가 y의 서브 set 맞냐?
# print(res)
#
# 결과값: True

from itertools import combinations

def solution(relation):
    # 속성 갯수를 가지고 조합을 구해야한다.
    N = len(relation[0])  # 속성 갯수
    M = len(relation)  # 튜플 갯수
    # 속성의 인덱스는 1부터 N까지
    keys = [i for i in range(0, N)]  # N=4면 [0, 1, 2, 3]
    candidate_keys = []
    # 속성들의 조합
    for i in range(1, N+1):  # 조합 요소 수가 1인 것부터 4인 것까지 순회
        for j in combinations(keys, i):  # i=2면 [(0,1), (0,2), (0,3), ...]
                                        # j = (0,1)
            # 유일성을 가지는 조합인지 검사
            tuple_list = list()
            for k in range(M):
                temp = [relation[k][l] for l in j]
                if temp in tuple_list:
                    break
                else:
                    tuple_list.append(temp)
            # 최소성을 가지는 조합인지 검사
            if len(tuple_list) == M:
                for keys in candidate_keys:
                    if set(keys).issubset(j):  # keys가 요소 수가 적은 조합이기 때문에 순서가 이럼
                        break
                else:
                    candidate_keys.append(j)
    return len(candidate_keys)



relation = [
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]
print(solution(relation))
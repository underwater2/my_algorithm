# 유일성에서 중복 검사, 최소성에서 이미 있는 조합에 포함되는지 검사하는 게 까다로웠다.
# tuple('abcd') => ('a', 'b', 'c', 'd')
# {2, 3} < {2, 3, 4} => True


from itertools import combinations

def solution(relation):
    answer = 0
    candidates = []  # 후보키 속성 조합을 set 요소로 저장
    for i in range(1, len(relation[0]) + 1):  # 전체 속성 중 몇 개(i)를 뽑아 조합을 만들 건지
        for comb in combinations(list(range(len(relation[0]))), i):  # 속성 인덱스들을 가지고 조합 만들기
            flag2 = 1
            for cand in candidates:  # (최소성 검사) 이미 있는 key 조합에 포함되는지 검사
                if set(comb) > cand:
                    flag2 = 0
                    break
            if flag2:  # 최소성 만족하면
                overlap = list()
                flag = 1
                for row in relation:  # 행 순회
                    data = list()
                    for c in comb:
                        data.append(row[c])
                    if data in overlap:  # (유일성 검사) 다른 행의 속성 조합과 같은지 검사
                        flag = 0
                        break
                    else:
                        overlap.append(data)
                if flag:
                    candidates.append(set(comb))
                    answer += 1

    return answer
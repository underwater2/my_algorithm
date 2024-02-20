# 완전탐색했더니 시간초과 나서 다른 풀이 참고
    # 풀이 출처
        # https://firsteast.tistory.com/103
        # 해시맵, 이진탐색 사용
    # 비슷한 경로로 푼 사람
        # https://velog.io/@dogcu/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-%EA%B2%80%EC%83%89

# [파이썬 기초] 유사 딕셔너리 defaultdict() 활용법
    # https://dongdongfather.tistory.com/69


from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []
    # 지원자가 속할 수 있는 모든 조건을 key로, 해당 조건에 속하는 지원자들의 점수들을 value로
    # key에 대해서 점수를 만족하는 지원자를 저장
    infos = defaultdict(list)
    for i in info:
        conditions = i.split()[:-1]
        score = int(i.split()[-1])
        for r in range(5):  # '-'로 몇 개(r) 바꿀 건지
            combis = list(combinations(range(4), r))  # '-'로 바꿀 경우의 수를 추출

            for c in combis:  # 각 경우에 수에 대해 '-'로 바꾼 조건을 생성
                test_cases = conditions[:]  # 리스트의 복사본 반환
                for v in c:
                    test_cases[v] = '-'
                infos['_'.join(test_cases)].append(score)
    for item in infos:
        infos[item].sort()  # 각 경우의 수에 따른 점수들 정렬

    for q in query:
        q = q.replace('and', '').split()
        conditions = '_'.join(q[:-1])  # 해시맵의 키
        score = int(q[-1])

        if conditions in list(infos):  # 조건이 가능한 경우의 수면
            data = infos[conditions]
            # 이분탐색 (변수 start 구할 때 bisect 라이브러리 사용 가능)
            # idx = bisect_left(target_list, target_score)
            if len(data) > 0:
                start, end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)
        else:
            answer.append(0)
    return answer
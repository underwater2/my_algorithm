# 정렬 문제
# 내림차순 정렬하고 처음부터 순회해가면서 답을 찾는다

def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    idx = 0
    while idx < len(citations):  # 인덱스 에러 방지
        if citations[idx] >= idx+1:
            answer = idx+1
            idx += 1
        else:
            break
    return answer
# 시간초과로 효율성 테스트 0점

# python] 문자열 split 여러번 적용하는 꿀팁 예제 설명-re.split
# https://gomming.tistory.com/18

import re
def solution(info, query):
    answer = []
    for idx, i in enumerate(info):
        info[idx] = i.split(" ")
    for idx, q in enumerate(query):
        query[idx] = re.split(r'\sand\s| ', q)
        count = 0
        for inf in info:
            if int(inf[4]) < int(query[idx][4]):
                continue
            flag = 0
            for i in range(0, 4):
                if query[idx][i] != '-':
                    if inf[i] != query[idx][i]:
                        flag = 1
                        break
            if not flag:
                count += 1
        answer.append(count)
    return answer
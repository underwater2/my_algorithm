def solution(k, tangerine):
    count = dict()
    for tan in tangerine:
        if (tan in count.keys()):
            count[tan] += 1
        else:
            count[tan] = 1
    answer = 0
    nums = 0
    cntList = sorted(list(count.values()))
    for i in range(len(cntList)-1, -1, -1):
        answer += 1
        nums += cntList[i]
        if nums >= k:
            return answer
    return answer
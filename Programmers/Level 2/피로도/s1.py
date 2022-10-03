from itertools import permutations

def solution(k, dgs):
    answer = 0
    for i in permutations(range(0, len(dgs)), len(dgs)):
        cnt = 0
        stat = k
        for p in i:
            if stat >= dgs[p][0]:
                cnt += 1
                stat -= dgs[p][1]
        answer = max(cnt, answer)
    return answer
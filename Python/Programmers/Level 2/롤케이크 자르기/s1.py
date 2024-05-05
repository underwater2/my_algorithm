from collections import Counter

def solution(topping):
    answer = 0
    cnt = Counter(topping)
    lset = set()
    rset = set(topping)
    for t in topping:
        lset.add(t)
        cnt[t] -= 1
        if cnt[t] == 0:
            rset.remove(t)
        if len(lset) == len(rset):
            answer += 1
    
    return answer

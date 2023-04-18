from collections import Counter

def solution(want, number, discount):
    wantList = dict(zip(want, number))
    
    answer = 0
    for i in range(0, len(discount)-9):
        dcList = Counter(discount[i:i+10])
        if wantList == dcList:
            answer += 1
    return answer
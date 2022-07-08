# 받은 문자열에서 가능한 단위 수를 모두 탐색
# 문자열 앞에서 뒤로 묶어가며 계산

def solution(s):
    if len(s) == 1:
        return 1

    answer = 987654321
    maxN = len(s) // 2

    for i in range(maxN, 0, -1):  # 최대묶음길이 ~ 1 까지 검색
        idx = i
        model = s[0:i]
        cnt = len(s)
        flag = 1
        for loop in range(len(s)//i-1):
            strs = s[idx:idx+i]
            if strs == model:
                cnt -= i
                flag += 1
                if loop == len(s)//i-2:  # 마지막 묶음인데 앞의 묶음와 같다면 <숫자 길이>를 더해줘야함
                    for x in ["1000", "100", "10", "1"]:
                        if flag // int(x):
                            cnt += len(x)
                            break
            else:
                if flag > 1:
                    for x in ["1000", "100", "10", "1"]:  # 같은 묶음들이 끝났다면 <숫자 길이>를 더해줌
                        if flag // int(x):
                            cnt += len(x)
                            break
                    flag = 1
            idx += i
            model = strs
        if answer > cnt:  # 최소 길이를 answer에 저장
            answer = cnt

    return answer
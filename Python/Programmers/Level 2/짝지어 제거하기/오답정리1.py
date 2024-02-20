# 스택 문제를 문자열 검색으로 시도함
# 반례
    # 입력값 〉	"abccccbaaa"
    # 기댓값 〉	1
# 반으로 접히는 부분의 위치 조건을 알 수 없어서 버린 코드


def solution(s):
    if len(s) % 2:  # 문자열 길이는 짝수여야함
        return 0

    answer = 1

    idx = 0
    flag = -1
    while idx < len(s) - 1:
        if flag == -1:
            if s[idx] == s[idx + 1]:
                idx += 2
            else:
                flag = idx
                idx += 1
        else:
            if s[idx] == s[idx + 1]:  # 반접히는 부분
                if len(s) - 1 >= 2 * idx - flag + 1:
                    if s[flag:idx + 1] == s[idx + 1:(2 * idx - flag + 2)][::-1]:
                        idx += (idx - flag + 2)
                        flag = -1
                    else:
                        return 0
                else:
                    return 0
            else:
                idx += 1

    if flag != -1:
        return 0

    return answer
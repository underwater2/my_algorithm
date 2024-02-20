# 스택/큐
# 스택 대신 flag라는 변수를 더하고 빼가는 방식 사용

def solution(string):
    flag = 0
    for s in string:
        if s == '(':
            flag += 1
        else:
            flag -= 1
        if flag < 0:  # )이 더 많음
            return False
    if flag != 0:  # (이 더 많음
        return False
    return True
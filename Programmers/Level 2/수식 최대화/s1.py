# split, eval을 사용해서 풀었다.
# 낮은 우선순위 연산자부터 split 해가면서, 높은 우선순위를 먼저 계산할 수 있게 함

answer = -1

def solution(exp):
    calc(exp, '*', '+', '-')  # 모든 경우의 수 넣기
    calc(exp, '*', '-', '+')
    calc(exp, '+', '*', '-')
    calc(exp, '+', '-', '*')
    calc(exp, '-', '*', '+')
    calc(exp, '-', '+', '*')
    return answer

def calc(exp, e1, e2, e3):  # e1 연산자는 마지막(newexp)에 표시되기 때문에 필요 없다.
    global answer
    exp = exp.split(e3)
    for i in range(len(exp)):
        newexp = exp[i].split(e2)
        for j in range(len(newexp)):
            newexp[j] = str(eval(newexp[j]))  # 가장 높은 우선순위 연산자 계산하고 다시 list에 넣음
        exp[i] = str(eval(e2.join(newexp)))  # 그 다음 높은 우선순위 연산자 계산하고 다시 list에 넣음
    if abs(eval(e3.join(exp))) > answer:  # 최종 계산값이 최댓값인지 확인
        answer = abs(eval(e3.join(exp)))

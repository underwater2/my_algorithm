# split, eval을 사용해서 풀었다.
# 낮은 우선순위 연산자부터 split 해가면서, 높은 우선순위를 먼저 계산할 수 있게 함

# 다른 풀이
    # 스택 2개 사용
        # https://latte-is-horse.tistory.com/132
    # 숫자, 연산자 따로 담고 계산 할때마다 del
        # https://velog.io/@yujin1760/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%EC%88%98%EC%8B%9D-%EC%B5%9C%EB%8C%80%ED%99%94

# expression을 숫자, 연산자로 나누어 리스트로 만드는 법
    # expression = re.split(r'(\D)',expression)
    # r'(\D)' regex ''에 들어가는 문자를 ()로 묶으면 사라지지 않고 리스트에 들어감.


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

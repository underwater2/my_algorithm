# 출처: 프로그래머스 다른 사람의 풀이
# split, eval을 사용한 점은 비슷하지만, 여기서는 문자열에 괄호를 넣어서 마지막에 eval을 해줬다.

def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
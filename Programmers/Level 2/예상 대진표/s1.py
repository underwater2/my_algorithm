# 1라운드씩 추가했을 때 번호가 어떻게 변하는지 규칙을 찾아 풀었다.

def solution(n,a,b):
    answer = 1  # 라운드 수
    if a > b:  a,b = b,a  # 항상 a<b 되도록 함
    while True:
        if (a+1)//2 == (b+1)//2:  # b-a == 1이 아니라 이 조건이어야 1 2 3 4 에서 2 3일 경우 등이 제외된다.
            return answer
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
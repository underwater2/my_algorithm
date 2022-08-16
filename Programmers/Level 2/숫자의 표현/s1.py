# 첫번째 숫자를 정해놓고 다음 숫자들을 하나씩 더해가면서 답을 구했다.

def solution(n):
    answer = 0
    for i in range(1, n//2+1):  # 첫번째 숫자는 연속된 수의 갯수가 2개일 수 있는 경우까지 탐색
        s, j = i, i
        while True:
            j += 1
            s += j
            if s == n:
                answer += 1
                break
            elif s > n:  # 합이 n보다 커지면 다음 첫번째 수로 넘어감
                break
    return answer+1  # 마지막에 자기 자신의 경우를 +1 한다.
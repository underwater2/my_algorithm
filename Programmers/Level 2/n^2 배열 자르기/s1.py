# 규칙은 잘 찾았지만 구현을 더 간단하게 할 수 있었던 문제

def solution(n, left, right):
    left_i = left // n
    left_j = left % n
    right_i = right // n
    right_j = right % n
    answer = []

    if left_i == right_i:
        for j in range(left_j, right_j + 1):
            answer.append(max(left_i, j) + 1)
    else:
        for j in range(left_j, n):
            answer.append(max(left_i, j) + 1)
        for i in range(left_i + 1, right_i):  # left와 right이 위치한 행 사이의 행들
            for j in range(n):
                answer.append(max(i, j) + 1)
        for j in range(0, right_j + 1):
            answer.append(max(right_i, j) + 1)
    return answer
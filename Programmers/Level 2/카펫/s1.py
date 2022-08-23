# 완전탐색
# 약수를 구해가면서 테두리 격자의 수를 맞춰봄

def solution(brown, yellow):
    if yellow == 1:
        return [3,3]
    for i in range(1, yellow//2+1):  # i는 노란격자의 높이
        if yellow / i == yellow // i:
            width = yellow // i
            height = i
            if 2*(width+height)+4 == brown:
                return [width+2, height+2]
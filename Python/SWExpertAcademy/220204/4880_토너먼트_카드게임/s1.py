# 이긴 가위바위보의 숫자를 먼저 구하고, 사람 숫자를 구할 수 있게 리스트를 튜플로 만들었다.
# 재귀호출인 건 알겠는데 어떤 방식으로 해야하는지 생각하는 데 오래걸렸다.

# 합병정렬 설명 (문제 안풀려서 찾아봤다.)
# https://zeddios.tistory.com/38

import sys
sys.stdin = open('sample_input.txt')

def divide(i, j):  # a에서의 인덱스
    global a
    if i == j:
        return a[i]
    elif i+1 == j:
        return rsp(a[i], a[j])
    return rsp(divide(i, (i+j)//2), divide((i+j)//2+1, j))


def rsp(p1, p2):
    if (p1[1], p2[1]) in [(1, 3), (2, 1), (3, 2)]:  # i가 이기는 경우
        return p1
    elif (p1[1], p2[1]) in [(1,2), (2,3), (3,1)]:  # j가 이기는 경우
        return p2
    else:
        return p1  # 비겼을 때는 숫자가 작은 것 선택


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))
    a = []
    for i in range(len(temp)):  # (인덱스+1, 가위바위보 숫자)로 된 리스트로 만들기
        a.append((i+1, temp[i]))
    print('#{} {}'.format(tc, divide(0, len(a)-1)[0]))


# # 답으로 이긴 사람의 가위바위보 숫자 잘 나오는 코드
# import sys
# sys.stdin = open('sample_input.txt')
#
# def divide(i, j):
#     global a
#     if i == j:
#         return a[i]
#     elif i+1 == j:
#         return rsp(a[i], a[j])
#     return rsp(divide(i, (i+j)//2), divide((i+j)//2+1, j))
#
#
# def rsp(p1, p2):
#     if (p1, p2) in [(1, 3), (2, 1), (3, 2)]:  # i가 이기는 경우
#         return p1
#     elif (p1, p2) in [(1,2), (2,3), (3,1)]:  # j가 이기는 경우
#         return p2
#     else:
#         return p1  # 비겼을 때는 숫자가 작은 것 선택
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     a = list(map(int, input().split()))
#     print(divide(0, len(a)-1))

# SWEA 파이썬 SW문제해결 기본 - Stack2 / 2차시 02 백트래킹
# a에 순열을 이루는 숫자를 넣어가면서 끝까지 반복. c 리스트를 이용. a의 value들이 순열 그 자체

def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True  # 이미 선택한 숫자는 쓰지 않는다. in_perm 요소가 1이면 그 인덱스 값은 다음 순열로 채택 안됨

    ncandidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:  # in_perm에 1이 없을수록 ncandidates가 큼
            c[ncandidates] = i  # 무조건 c[0]부터 숫자 채워짐
            ncandidates += 1  # 다음 인덱스로 and 넣을 숫자 수 증가
    return ncandidates


# Power Set 풀이랑 같음
def backtrack(a, k, input):  # a: 순열 만들 틀 리스트, k: 결정된 요소의 수, input: 순열 구할 요소들의 수
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:  # 다 선택했으면
        process_solution(a, k)  # 문제에서 원하는 조치를 하면 됨
    else:
        k += 1  # 1 -> input
        ncandidates = construct_candidates(a, k, input, c)  # c를 추가로 데리고감
        for i in range(ncandidates):  # k가 커질수록 선택할 수 없는 숫자가 적어짐
            a[k] = c[i]
            backtrack(a, k, input)  # 재귀


def process_solution(a, k):  # 순열 콘솔에 print
    print('(', end='')
    for i in range(1, k+1):
        print(a[i], end=' ')
    print(')')


MAXCANDIDATES = 100
NMAX = 100  # input을 몇으로 할지 모르니 넉넉하게 100으로 설정한듯
a = [0] * NMAX
backtrack(a, 0, 3)  # a를 틀으로 순열 만들 것, 아직 아무요소도 결정하지 않았으므로 k는 0, 3개 요소를 가지고 순열 구할 것
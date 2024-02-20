# SWEA 파이썬 SW문제해결 기본 - Stack2 / 2차시 02 백트래킹
# a에 1을 번갈아가며 넣음. value가 1인 곳의 요소만 부분집합에 포함시킴.(index 같은 것) c 리스트를 이용.

def construct_candidates(a, k, input, c):
    c[0] = True  # 1
    c[1] = False  # 0
    return 2  # backtrack으로 돌아가서 range 안에 쓰이게 됨


def backtrack(a, k, input):  # a: 부분집합 만들 틀 리스트, k: 결정된 요소의 수, input: 부분집합 구할 요소들의 수
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES  # 1. 매번 여기서 초기화해주는 이유를 모르겠다.

    if k == input:  # 다 선택했으면
        process_solution(a, k)  # 문제에서 원하는 조치를 하면 됨
    else:
        k += 1  # 1 -> input
        ncandidates = construct_candidates(a, k, input, c)  # c를 추가로 데리고감
        for i in range(ncandidates):  # i: 0 -> 1
            a[k] = c[i]  # a의 인덱스 1번부터 input번까지 0과 1을 번갈아 주게됨
            backtrack(a, k, input)  # 재귀


def process_solution(a, k):  # 부분집합 콘솔에 print
    print('(', end='')
    for i in range(k+1):
        if a[i]:  # i 인덱스에서 값이 1일 경우
            print(i, end=' ')  # 부분집합에 속함
    print(')')


MAXCANDIDATES = 100  # 2. c는 c[0], c[1] 밖에 안쓰이는데 왜 길이를 100으로하는지 모르겠다.
NMAX = 100  # input을 몇으로 할지 모르니 넉넉하게 100으로 설정한듯
a = [0] * NMAX
backtrack(a, 0, 3)  # a를 틀으로 부분집합 만들 것, 아직 아무요소도 결정하지 않았으므로 k는 0, 3개 요소를 가지고 부분집합 구할 것
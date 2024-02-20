# 시간초과
# 중복되는 순열들을 해결하지 못해서 계속 시간초과가 난 것 같다.

import sys
sys.stdin = open('input.txt')

from collections import deque

def calc(n1, n2, oper):
    if oper == 0:
        return n1 + n2
    elif oper == 1:
        return n1 - n2
    elif oper == 2:
        return n1 * n2
    elif oper == 3:
        if n1 < 0:
            temp = -n1 // n2
            return -temp
        return n1 // n2


N = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
newo = []
for i in range(4):
    newo.extend([i] * operator[i])

minV = 987654321
maxV = -987654321

sel = [0] * (N-1)  # 결과들이 저장될 리스트
check = [0] * (N-1)  # 해당 원소를 이미 사용했는지 안했는지 체크

queue = deque()
cnt = 0

def perm(idx):
    global minV, maxV, cnt
    # 다 뽑아서 정리했다면
    if idx == N-1:
        print(sel)
        cnt += 1
        print(cnt)
        # print(queue[-1])
        result = queue[-1]
        if result > maxV:
            maxV = result
        if result < minV:
            minV = result
    else:
        for i in range(N-1):
            if check[i] == 0:
                sel[idx] = newo[i]  # 값을 써라
                check[i] = 1  # 사용했다는 표시
                # queueLen = len(queue)
                if idx == 0:
                    queue.append(calc(num[0], num[1], sel[0]))
                else:
                    queue.append(calc(queue[-1], num[idx+1], sel[idx]))
                perm(idx+1)
                check[i] = 0  # 다음 반복문을 위한 원상복구
                queue.pop()

perm(0)


print(maxV)
print(minV)



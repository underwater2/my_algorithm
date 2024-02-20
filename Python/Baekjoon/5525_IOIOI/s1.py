# S를 순회하며 I인 곳마다 하나하나 탐색을 하면 너무 오래걸릴 것 같아서 규칙을 찾아봤다.

# S[i:i+2] 이런 부분에서 인덱스 에러가 나올 거라고 예상했는데,
# print 해보니 문자열의 인덱스를 넘어가면 존재하는 문자열까지만 slicing해서 반환해줬다.

import sys
sys.stdin = open('input.txt')

N = int(input())
M = int(input())
S = input()

flag = 0
i = 0
li = list()
while i < M:  # i는 S의 인덱스
    if flag == 0:
        if S[i:i+3] == 'IOI':
            flag = 1
            i += 3
        else:
            i += 1
    else:
        if S[i:i+2] == 'OI':
            flag += 1
            i += 2
        else:
            li.append(flag)
            flag = 0

result = 0
for j in li:
    if j >= N:
        result += j-N+1
print(result)


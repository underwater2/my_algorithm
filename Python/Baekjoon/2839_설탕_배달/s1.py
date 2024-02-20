# Greedy
# 5크기 봉지를 최대로 설정한 후에, 한개씩 줄여가며 3크기 봉지에 딱 들어 맞는지 조사한다.
# 맞는 조합이 있으면 그 시점에 검색을 중단하고 답을 출력한다.

import sys
sys.stdin = open('input.txt')

N = int(input())

A = N//5
result = -1
for a in range(A, -1, -1):
    M = N - 5*a
    if not M % 3:
        result = a + M//3
        break
    else:
        continue
print(result)


# # 검색해서 나온 다른 풀이. 이 풀이도 신기했다
# num = int(input())
# count = 0
#
# while num >= 0:
#   if num % 5 == 0:
#     count += int(num // 5)
#     print(count)
#     break
#
#   num -= 3
#   count += 1
#
# else:
#   print(-1)
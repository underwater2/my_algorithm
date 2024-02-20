# 출처: 프로그래머스 다른 사람의 풀이
# 뒤의 수와 비교하되, 제거해주고나서 이전에 봤던 숫자로 돌아가서 계속 비교한다.

def solution(number, k):
    i = 0
    while i < len(number) - 1 and k > 0:
        if number[i] < number[i + 1]:
            number = number[:i] + number[i + 1:]
            if i != 0:
                i -= 1  # 이 부분이 핵심
            k -= 1
        else:
            i += 1
    if k > 0:
        return number[:-k]
    return number

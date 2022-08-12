# 내용 출처: https://velog.io/@koyo/python-is-prime-number

# 에라토스테네스의 체
# 이는 범위에 대한 소수 판별에 유리하다. 하는 방법은 다음과 같다.
#
# 2부터 N까지의 모든 자연수를 나열한다.
# 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
# 남은 수 중에서 i의 배수를 모두 제거한다.(i는 제거하지 않는다.)
# 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.
# 에라토스테네스의 체 알고리즘의 시간 복잡도는 O(NloglogN)으로 사실상 선형 시간에 동작할 정도로 빠르다. 하지만, N크기 만큼의 메모리를 저장하고 기억해야하므로 주의해야한다.

import math

# 소수 판별 함수(에라토스테네스의 체)
def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]

# N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함

print(is_prime_number(26))
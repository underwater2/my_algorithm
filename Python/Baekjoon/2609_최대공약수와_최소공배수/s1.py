# 최대공약수와 최소공배수 함수 직접 만들기
    # https://st-lab.tistory.com/154
        # 유클리드 호제법으로 도출
        # 최대공약수는 n1 >= n2일 때 gcd(n1, n2) = gcd(n2, n1 % n2) 정리에서 유도된다
        # 최소공배수 = n1 * n2 / 최대공약수

import sys
sys.stdin = open('input.txt')

import math

n1, n2 = map(int, sys.stdin.readline().rstrip().split())

print(math.gcd(n1, n2))
print(math.lcm(n1, n2))
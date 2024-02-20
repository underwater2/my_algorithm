import sys
sys.stdin = open('input.txt')

price = int(input())
change = 1000 - price
cnt = 0
coin = [500, 100, 50, 10, 5, 1]

for c in coin:
    cnt += change // c
    change %= c

print(cnt)
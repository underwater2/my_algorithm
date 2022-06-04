import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

tp = [0]
for _ in range(N):
    tp.append(list(map(int, sys.stdin.readline().split())))

print(tp)
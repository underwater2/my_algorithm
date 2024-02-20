# greedy

import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().rstrip().split())

book = list(map(int, sys.stdin.readline().rstrip().split()))

book_sort = sorted(book)

book_minus = []
book_plus = []

for b in range(0, N):
    if book_sort[b] > 0:
        book_minus = book_sort[:b]
        book_plus = book_sort[b:]
        break
    else:
        book_minus = book_sort

ans = 0

if book_minus:
    idx = 0
    while idx <= len(book_minus)-1:
        ans += -book_minus[idx] * 2
        idx += M

if book_plus:
    idx = len(book_plus)-1
    while idx >= 0:
        ans += book_plus[idx] * 2
        idx -= M

if len(book_plus) == 0:
    ans -= -book_minus[0]
elif len(book_minus) == 0:
    ans -= book_plus[-1]
elif -book_minus[0] > book_plus[-1]:
    ans -= -book_minus[0]
else:
    ans -= book_plus[-1]

print(ans)


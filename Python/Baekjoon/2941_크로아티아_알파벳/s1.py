import sys
sys.stdin = open('input.txt')

alphabet = sys.stdin.readline().rstrip()

alphabet += '00'

flag = 0
ans = 0
idx = 0
while idx < len(alphabet)-2:
    al = alphabet[idx]

    if al == 'c':
        if alphabet[idx+1] in ['=', '-']:
            idx += 1
    elif al == 'd':
        if alphabet[idx:idx+3] == 'dz=':
            idx += 2
        elif alphabet[idx+1] == '-':
            idx += 1
    elif al in ['l', 'n']:
        if alphabet[idx+1] == 'j':
            idx += 1
    elif al in ['s', 'z']:
        if alphabet[idx + 1] == '=':
            idx += 1
    ans += 1
    idx += 1

print(ans)

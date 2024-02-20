s, e = map(int, input().split())

while not 2 <= s <= 9 or not 2 <= e <= 9:
    print('INPUT ERROR!')
    s, e = map(int, input().split())


for i in range(1, 10):
    if s < e:
        for j in range(s, e):
            if j * i < 10:
                print(f'{j} * {i} =  {j * i}', end='   ')
            else:
                print(f'{j} * {i} = {j * i}', end='   ')
        if j == e-1:
            if e * i < 10:
                print(f'{e} * {i} =  {e * i}')
            else:
                print(f'{e} * {i} = {e * i}')
    elif s == e:
        if e * i < 10:
            print(f'{e} * {i} =  {e * i}')
        else:
            print(f'{e} * {i} = {e * i}')
    else:
        for j in range(s, e, -1):
            if j * i < 10:
                print(f'{j} * {i} =  {j * i}', end='   ')
            else:
                print(f'{j} * {i} = {j * i}', end='   ')
        if j == e+1:
            if e * i < 10:
                print(f'{e} * {i} =  {e * i}')
            else:
                print(f'{e} * {i} = {e * i}')


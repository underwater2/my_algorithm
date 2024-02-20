# import re
# # 아래 두 줄은 같다.
# print(re.split('\s+', s))
# print(s.split())

def solution(s):
    s = list(s)
    flag = 0
    for i in range(len(s)):
        if s[i] == ' ':
            flag = 0
        else:
            if flag:
                s[i] = s[i].lower()
            else:
                s[i] = s[i].upper()
                flag = 1
    return ''.join(s)
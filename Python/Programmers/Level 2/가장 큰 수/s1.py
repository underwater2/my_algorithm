# 처음에는 4자리수로 맞춰줄 때, 가장 앞자리 숫자를 더해줬다. => 오답
    # 반례 [232, 23] "23232"
# 다른 풀이에서 힌트를 얻어 앞자리부터 순서대로 원래 숫자를 더해줌 => 정답
    # 이 방식을 사용했을 때 정렬이 잘 되는 이유는?
        # (정리) 만약 숫자가 한자리라면, *3으로 적어도 3자리 이상 만들어줘야 다른 숫자들과 앞자리부터 3자리를 비교할 수 있다. 3자리보다 길어져도 앞자리만 비교하면 되니 상관없다.
        # 각 num의 자릿수가 1000이하이니까요! 가령 9, 991 이면 9에다가 *2해도 99, 991로 여전히 991이 더 앞편에 정렬되기 때문입니다.
        # 만일 numbers가 [221,2,10] 이렇게 주어졌다고 가정했을때 x*2를 하면 [221221,22,1010],,,이렇게 되면 22보다 221이 문자열 비교해도 더 큰수로 나오기 때문에 원하는 정렬이 되지 않습니다. 100이하라면 모를까 1000이하의 조건이라면 x*3을 해줘야 하고, 10000이하의 조건이라면 x*4를 해줘야 하지 않을까요?
        # 숫자를 반복시키는 이유는 앞에서부터 같은 숫자패턴이 존재하는 숫자들의 비교를 위해서입니다. 기존 숫자를 반복시키게 되면 그 숫자가 앞에 왔을 때 만들 수 있는 최대 숫자를 만들 수 있습니다.
# 나랑 비슷한 경로로 해결한 글
    # https://dailyheumsi.tistory.com/102
# functools.cmp_to_key 사용한 풀이
    # https://velog.io/@heyday_7/python-%EC%A1%B0%EA%B1%B4-%EC%A0%95%EB%A0%AC-%ED%95%98%EA%B8%B0-cmptokey

def solution(numbers):
    strings = []
    # 튜플 (4자리를 맞춰놓은 숫자, 더해놓은 글자 길이) 만들기 <= 여기서 굳이 4자리를 맞추지 않아도 정렬은 잘된다.
    for number in numbers:
        number = str(number)
        plus = 4 - len(number)
        while len(number) != 4:
            if len(number) > 4:
                number = number[:4]
            elif len(number) < 4:
                number *= 4
        tup = (number, plus)
        strings.append(tup)

    strings = sorted(strings, key=lambda x: x[0], reverse=True)
    answer = ''
    for string in strings:
        answer += string[0][:4 - string[1]]  # 붙여줬던 문자열을 자르고 붙인다.
    if answer[0] == '0':  # 반례 [0, 0, 0, 0, 0, 0] "0"
        answer = '0'
    return answer
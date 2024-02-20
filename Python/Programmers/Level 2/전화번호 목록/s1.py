# 해시 문제인데 안쓰고 풀었다.
# 해시로 풀기
    # dict에 가능한 전화번호를 모두 넣고 하나씩 비교함
# 정규식에서 ^는 문자열의 처음, $는 문자열의 마지막을 의미.
    # 예를 들어 정규식이 ^python인 경우 문자열의 처음은 항상 python으로 시작해야 매치됨
    # 정규식이 python$이라면 문자열의 마지막은 항상 python으로 끝나야 매치된다

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
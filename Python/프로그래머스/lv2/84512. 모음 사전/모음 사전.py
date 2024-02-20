def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    words = ['','','','','']
    
    num = 0
    for w1 in vowels:
        words[0] = w1
        num += 1
        if word == "".join(words):
            return num
        print("".join(words))
        for w2 in vowels:
            words[1] = w2
            num += 1
            if word == "".join(words):
                return num
            for w3 in vowels:
                words[2] = w3
                num += 1
                if word == "".join(words):
                    return num
                for w4 in vowels:
                    words[3] = w4
                    num += 1
                    if word == "".join(words):
                        return num
                    for w5 in vowels:
                        words[4] = w5
                        num += 1
                        if word == "".join(words):
                            return num
                    words[4] = ""
                words[3] = ""
            words[2] = ""
        words[1] = ""
    return num

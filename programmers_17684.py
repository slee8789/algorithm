import sys


def solution(msg):
    sys.setrecursionlimit(2000)
    global switch
    dict = [chr(i + 65) for i in range(26)]
    answer = []

    for index, word in enumerate(msg):
        # if word in answer:
        #     check_contains(dict, msg, len(msg) + index + 1, msg[index:len(msg) + index + 1], len(msg[index:len(msg) + index + 1]), answer)
        # else:

        if switch > 0:
            switch -= 1
            continue

        check_contains(dict, msg, index, word, len(word), answer)

    result = []
    for value in answer:
        result.append(dict.index(value) + 1)

    print(dict)
    return result


global temp_list
temp_list = []
global switch
switch = 0


def check_contains(dict, msg, index, target_word, length, answer):
    global temp_list
    global switch
    if target_word in dict:
        # if target_word not in answer:
        # answer.append(target_word)
        print("1test ", index, len(msg) - 1, temp_list)
        if index < len(msg) - 1:
            if len(target_word) > 1:
                switch += 1
            temp_list.append(target_word)
            print(target_word, msg[index:length + index + 1])
            check_contains(dict, msg, index, msg[index:length + index + 1], len(msg[index:length + index + 1]), answer)

        else:
            print("test   ", target_word)
            answer.append(target_word)
    else:
        # dict.append(target_word)
        dict.append(target_word)
        answer.append(temp_list.pop())
        index += 1


# KAKAO

# DICT      KA  AK  KAO
# ANSWER    K   A   KA  O

# KAKBO

# DICT      KA  AK  KB
# ANSWER    K   A   K


# print(solution('KAKAO'))
# print(solution('KAKBO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
# print(solution('ABABABABABABABAB'))
# print(solution('TESTE'))

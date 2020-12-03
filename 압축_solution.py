from string import ascii_uppercase

# for i, upper in enumerate(ascii_uppercase):
#     print(i, upper)

dic = {upper: i+1 for i, upper in enumerate(ascii_uppercase)}
# print(dic)
def process(text, stack=''):
    # print(stack, text)

    if not text:
        return dic[stack], text
    else:
        stack += text[0]
        text = text[1:]
        if stack not in dic.keys():
            dic[stack] = len(dic) + 1
            print(stack[:-1])
            return dic[stack[:-1]], stack[-1] + text
        else:
            return process(text, stack)

def solution(msg):
    answer = []
    text = msg[:]
    while True:
        res, text = process(text)
        # print(res, text)
        answer.append(res)
        if not text:
            return answer
# print(dic)
print(solution('KAKAO'))
# print(solution('TOBEORNOTTOBEORTOBEORNOT'))
# print(solution('ABABABABABABABAB'))
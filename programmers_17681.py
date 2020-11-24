# print(list(bin(9)[2:].rjust(5,'0')))

def solution(n, arr1, arr2):
    arr3 = [0 for _ in range(n)]
    print(arr3)

    for i in range(n):
        arr3[i] = arr1[i] | arr2[i]
    a = 1 << n
    ans = []
    for i in range(n):
        x = a | arr3[i]
        s = []
        for j, w in enumerate(format(x, 'b')):
            if j == 0:
                continue
            if w == '1':
                s.append('#')
            else:
                s.append(' ')
        ans.append(''.join(s))
    return ans

result = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
print(result)


# 이진수 변환
# 변환된 5자리 리스트로 변환
# 같은 인덱스의 벨류끼리 OR 연산
# 결과 리스트를 String으로 변환
# 변환된 String값중 1을 '#', 0을 ' '으로 치환
# 출력


# n : n진법
# t : 미리구할 숫자의 갯수
# m : 게임에 참가하는 인원
# p : 튜브의 순서

# def change_system(num, system):
#     table = "0123456789ABCDEF"
#     value, rest = divmod(num, system)
#     # print(value, rest)
#     result = ''
#     if value >= system:
#         result += table[rest]
#         change_system(value, system)
#     else value < system:
#
#     return result

def numeral_system(number, base):
    table = "0123456789ABCDEF"
    q, r = divmod(number, base)
    n = table[r]
    return numeral_system(q, base) + n if q else n


def solution(n, t, m, p):
    answer = ''
    num = 0
    board = ''
    while True:
        board += numeral_system(num, n)
        num += 1
        if t * m < len(board):
            break

    for i in range(0, len(board), m):
        if len(answer) < t:
            answer += board[i + p - 1]

    return answer


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))

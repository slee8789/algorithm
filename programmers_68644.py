def solution(numbers):
    from itertools import combinations
    # return sorted(list(set(lambda x: x[0]+x[1],list(combinations(numbers,2)))))
    return sorted(list(set(map(lambda x: x[0]+x[1],list(combinations(numbers, 2))))))


print(solution([2,1,3,4,1]))



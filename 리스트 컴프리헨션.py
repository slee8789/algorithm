array = [i for i in range(10)]
print(array)

array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i * i for i in range(10)]
print(array)

# 2차원 리스트를 초기화할 때 효과적으로 사용할 수 있다.
# N * M 크기의 2차원 리스트를 한 번에 초기화 해야 할 때 유용

n, m = 3, 3
array = [[0] * m for _ in range(n)]
print(array)

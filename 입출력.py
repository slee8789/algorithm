# 자주 사용되는 표준입력 방법
# input() 함수는 한 줄의 문자열을 입력 받는 함수입니다.
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용합니다.

# 예시) 공백을 기준으로 구분된 데이터를 입력 받을 때는 다음과 같이 사용합니다.
# list(map(int, input().split()))

# 입력 : 1 2 3 4 5

# input().split() : ['1','2','3','4','5']
# map(int, input().split()): map([1, 2, 3, 4, 5])

a, b, c, d, e = map(int, input().split())
print(a, b, c, d, e)

# sort 와 sorted
a = [5, 2, 4, 6, 8]

a.sort()

print(a)

a = [5, 2, 4, 6, 8]
b = sorted(a)

print(a)
print(b)


#리스트에서 특정 값의 원소를 모두 제거하기
a = [1,2,3,4,5,5,5]
remove_set = [3,5]

result = [i for i in a if i not in remove_set]
print(result)



# n,m = list(map(int, input().split(' ')))
# data = list(map(int, input().split(' ')))

# n, m = 5, 21
# data = [5, 6, 7, 8, 9]

n, m = 10, 500
data = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]

from itertools import combinations

result = list(combinations(data, 3))

value = 0
for x, y, z in result:
    if x + y + z <= m:
        value = max(value, x + y + z)

print(value)

# sum()

# min(), max()

# eval()

# sorted()

# 순열과 조합

# n P r

from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

result = list(permutations(data, 3))

print(result)

# n C r

result = list(combinations(data, 2))

print(result)

# 중복 순열

result = list(product(data, repeat=2))

print(result)

# 중복 조합

result = list(combinations_with_replacement(data, 2))

print(result)

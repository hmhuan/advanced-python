from itertools import count, cycle, repeat
from itertools import groupby
import operator
from itertools import accumulate
from itertools import combinations, combinations_with_replacement
from itertools import permutations
from itertools import product
prod = product([1, 2], [3, 4])
print(list(prod))

prod = product([1, 2], [3], repeat=2)
print(list(prod))

permutation = permutations([1, 2, 3])
print(list(permutation))

permutation = permutations([1, 2, 3], 2)
print(list(permutation))

combination = combinations([1, 2, 3, 4], 2)
print(list(combination))

combination = combinations_with_replacement([1, 2, 3, 4], 2)
print(list(combination))

acc = accumulate([1, 2, 3, 4])
print(list(acc))

acc = accumulate([1, 2, 3, 4], func=operator.mul)
print(list(acc))

acc = accumulate([1, 5, 2, 3, 7, 4, 12, 3, 1], func=max)
print(list(acc))

acc = accumulate([1, 5, 2, 3, 7, 4, 12, 3, 1], func=min)
print(list(acc))


def smaller_than_3(x):
    return x < 3


group_obj = groupby([1, 2, 3, 4], key=smaller_than_3)
for key, group in group_obj:
    print(key, list(group))
    pass


for i in count(10):
    print(i)
    if (i >= 12):
        break
    pass
sum = 0
for i in cycle([1, 2, 3]):
    print(i)
    sum += i
    if (sum >= 12):
        break
    pass

for i in repeat("H", 4):
    print(i)
    pass

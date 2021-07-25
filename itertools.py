from itertools import product
prod = product([1,2], [3,4])
print(list(prod))

prod = product([1,2], [3], repeat=2)
print(list(prod))

from itertools import permutations
permutation = permutations([1,2,3])
print(list(permutation))

permutation = permutations([1,2,3], 2)
print(list(permutation))

from itertools import combinations, combinations_with_replacement
combination = combinations([1,2,3,4], 2)
print(list(combination))

combination = combinations_with_replacement([1,2,3,4], 2)
print(list(combination))

from itertools import accumulate
acc = accumulate([1,2,3,4])
print(list(acc))

import operator
acc = accumulate([1,2,3,4], func=operator.mul)
print(list(acc))

acc = accumulate([1,5,2,3,7,4, 12, 3, 1], func=max)
print(list(acc))

acc = accumulate([1,5,2,3,7,4, 12, 3, 1], func=min)
print(list(acc))

from itertools import groupby
def smaller_than_3(x):
    return x < 3

group_obj = groupby([1,2,3,4], key=smaller_than_3)
for key, group in group_obj:
    print(key, list(group))
    pass

from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if (i >= 12):
        break
    pass
sum  = 0
for i in cycle([1,2,3]):
    print(i)
    sum += i
    if (sum >= 12):
        break
    pass

for i in repeat("H", 4):
    print(i)
    pass

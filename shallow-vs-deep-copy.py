# assignment operator
import copy
list_a = [1, 2, 3]
list_b = list_a
list_b.append(4)
print(list_a)  # [1,2,3,4]

list_a[0] = 0
print(list_a)  # [0,2,3,4]
print(list_b)  # [0,2,3,4]

# Shallow copy
list_a = [1, 2, 3]
list_b = copy.copy(list_a)
list_b.append(4)
print(list_a)  # [1,2,3]

list_a[0] = 0
print(list_a)  # [0,2,3]
print(list_b)  # [1,2,3,4]

list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.copy(list_a)

# affects the other!
list_a[0][0] = -10
print(list_a)
print(list_b)

# not affect but too ugly
list_a[0] = [10, 2, 3, 4, 5]
print(list_a)
print(list_b)

# shallow copies
list_b = list_a.copy()
list_b = list_a[:]

# Deep copy -> use deepcopy()
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.deepcopy(list_a)

list_a[0][0] = 0
print(list_a)
print(list_b)

# should you deep copy when clone object

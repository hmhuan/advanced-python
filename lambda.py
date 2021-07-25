def add_ten(x): return x + 10


val1 = add_ten(5)
val2 = add_ten(10)
print(val1, val2)  # 15 20


def mul(x, y): return x * y


val1 = mul(2, 3)
val2 = mul(30, 21)
print(val1, val2)

# useage lambda inside another function
def add_func(y):
    return lambda x: x + y
    pass


add_3 = add_func(3)
print(add_3(1))  # 4

add_10 = add_func(10)
print(add_10(100))  # 110

# custom sorting using lambda fucntion as key parameter
point2ds = [(1, 9), (4, 1), (5, -3), (10, 2)]
sorted_by_y = sorted(point2ds, key=lambda x: x[1])
print(sorted_by_y)

my_list = [-1, 2, 0, -3, 4, -2, 1, 4, 5]
sort_abs = sorted(my_list, key= lambda x: abs(x))
print(sort_abs)

# using lambda for map function
a = [1,2,3,4,5,6,7,8]
b = list(map(lambda x: x * 2, a)) # b = [x * 2 for x in a]
print(b)

# using lambda for filter function
a = [1,2,3,4,5,6,7,8]
b = list(filter(lambda x: x %2 == 0, a)) # b = [x for x in a if x % 2 == 0]
print(b)

# using lambda for reduce function
from functools import reduce
a = [1,2,3,4,5]
product_a = reduce(lambda x, y: x * y, a) # 120
print(product_a)

sum_a = reduce(lambda x, y: x + y, a) # 15
print(sum_a)
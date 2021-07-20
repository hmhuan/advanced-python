tuple_1 = ("Michael", 19, "Australia")
tuple_2 = ("Merlin", 20, "Thailand")

print(tuple_1)
print(tuple_2)

tuple_3 = ([1, 2, 3])
print(tuple_3)

# access tuple element
item = tuple_1[0]
print(item)

# tuple cannot be changed -> immutable
item = 3
print(item)
# tuple_1[0] = 1
# print(tuple_1)

# delete tuple
# del tuple_1
# print(tuple_1)

# iterating in tuple
for element in tuple_1:
    print(element)
    pass

# check if element in tuple
print("Angelo" in tuple_1)
print(19 in tuple_1)

# useful methods
my_tuple = ('b', 'a', 'n', 'a', 'n', 'a')
print(len(my_tuple))
print(my_tuple.count('a'))
print(my_tuple.index('n'))

my_tuple = (1, 2) * 3
print(len(my_tuple))
print(my_tuple)

my_tuple = (1, 2, 3) + (4, 5, 6) + (2, 4)
print(my_tuple)

# convert to list
my_tuple = ('a', 1, 'b', 2, 'c', 3)
my_list = list(my_tuple)
print(my_list)

# convert string to tuple
string_to_tuple = tuple('a1b2c3')
print(string_to_tuple)



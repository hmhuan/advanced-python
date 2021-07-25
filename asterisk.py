# multiple and power operations
print(2 * 4)
print(2 ** 4)

# Creation default list, string
zeros = [0] * 8
print(zeros) 

onetwos = (1, 2) * 10
print(onetwos)

AB_string = 'AB' * 5
print(AB_string)

# *args, **kwargs (keyword args)
def my_func(*args, **kwargs):
    for arg in args:
        print(arg)
        pass
    for key in kwargs:
        print(key, kwargs[key])
        pass
    pass

my_func("abc", 12, 4, [1, 2, 3, 4], name="Alpas", age=19)

# Parameters after '*' or '*identifier' are keyword-only parameters and may only be passed using keyword arguments.
def my_func_2(name, *identifier, age):
    print(name)
    print(age)
    pass

my_func_2("Grafana", age=20)

# unpacking for fucntion arguments
def foo(a,b,c):
    print(a,b,c)

my_list = [1,2,3]
foo(*my_list)

my_string = "ABC"
foo(*my_string)

my_dictionary = {0: 'A', 1: 'B', 2: 'C'}
foo(*my_dictionary)

# unpacking container
numbers = [1,2,3,4,5,6,7,8]
*begin, end = numbers
print(begin, end)

begin, *end = numbers
print(begin, end)

first, *mid, last = numbers
print(first, mid, last)

# merge iterables
my_tuple = (1,2,3)
my_set = {3, 4, 5}
my_list = [*my_tuple, *my_set]
print(my_list)

# merge two dictionaries with dict unpacking
dict_a = {'one': 1, 'two': 2}
dict_b = {'three': 3, 'four': 4}
dict_c = {**dict_a, **dict_b}
print(dict_c)


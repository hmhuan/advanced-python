
# template for generator
def my_generator():
    yield 1
    yield 2
    yield 3
    pass

def count_down(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1
        pass

cd = count_down(3)
print(next(cd))
print(next(cd))
print(next(cd))

cd = count_down(4)
for i in cd:
    print(i)

cd = count_down(3)
sum_cd = sum(cd)
print(sum_cd)

cd = count_down(4)
list_cd = list(cd)
print(list_cd)

# Generator save memory
import sys 

def firstn_list(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1

    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

n = 100000
sum_of_first_n = sum(firstn_list(n))
print(sum_of_first_n)
print(sys.getsizeof(firstn_list(n)))

sum_of_first_n = sum(firstn_generator(n))
print(sum_of_first_n)
print(sys.getsizeof(firstn_generator(n)))

# another example for fibonacci numbers
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

fib = fibonacci(100)
print(list(fib))

# Generator expression
my_generator = (i for i in range(10000) if i % 2 == 0)
print(sys.getsizeof(my_generator), "bytes")

my_list = [i for i in range(10000) if i % 2 == 0]
print(sys.getsizeof(my_list), "bytes")

# Concept behind a generator  __iter__, __next__

class firstn:
    def __init__(self, n):
        self.n = n
        self.num = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num < self.n:
            curr = self.num
            self.num += 1
            return curr
        else:
            raise StopIteration()

firstn_object = firstn(1000)
print(sum(firstn_object))

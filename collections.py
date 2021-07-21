# Counter
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import Counter
a = [1, 0, 2, 4, 3, 2, 4, 1, 1, 4, 20, 1, 4, 0]
my_counter = Counter(a)

print(my_counter)
print(my_counter.items())
print(my_counter.keys())  # should be cast to list
print(my_counter.values())  # should be cast to list

print(my_counter.most_common())  # not pass will return sort by value -> key

print(list(my_counter.elements()))

# namedtuple
Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt)
print(pt._fields)
print(type(pt))
print(pt.x, pt.y)

Person = namedtuple('Person', 'name, age, job')
person = Person('Mike', 22, 'engineer')
print(person)
for element in person:
    print(type(element))
    pass

# OrderedDict
ordinary_dict = {}
ordinary_dict['a'] = 1
ordinary_dict['f'] = 4
ordinary_dict['c'] = 3
ordinary_dict['d'] = 2
ordinary_dict['e'] = 5
# this may be in orbitrary order prior to Python 3.7
print(ordinary_dict)

ordered_dict = OrderedDict(ordinary_dict)
print(ordered_dict)
# same functionality as with ordinary dict, but always ordered
for k, v in ordinary_dict.items():
    print(k, v)

# defaultdict
d = defaultdict(int, {0: 1, 1: 2, 2: 3})
print(d)
print(d[4])

# deque
d = deque()

d.append(1)
d.append('a')
print(d)

d.appendleft('b')
print(d)

print(d.pop())
print(d)

print(d.popleft())
print(d)

d.extend([1, 2, 3, 4])  # append every element
d.extendleft([0, 2, 3])  # it push every element to the left
print(d)

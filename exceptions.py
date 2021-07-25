# rasing an exception
from copy import Error


x = -5
# if x < 0:
#     raise Exception('x should not be negative')
#     pass

# assert
x = -5
# assert(x >= 0), 'x is not positive'

try:
    a = 5 / 0
except:
    print('some error occured.')
    pass
finally:
    print('it is always appear.')
    pass

try:
    a = 5 / 0
    pass
except Exception as e:
    print(e)
    pass

try:
    a = 5 / 1
    b = a + '11'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

# else clause
try:
    a = 5 / 1
    pass
except Exception as e:
    print(e)
    pass
else:
    print('everything is ok')

# Define Exception
class ValueIsNotPositive(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
        pass
    pass

def test_value(x):
    if x < 0:
        raise ValueIsNotPositive('value is negative', x)
        pass
    pass
try:
    test_value(-19)
    pass
except ValueIsNotPositive as e:
    print(e.message, '\nThe value is:', e.value)


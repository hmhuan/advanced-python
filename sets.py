# This is sets 101
my_set = {"pomme", "orange", "chocolat", "gateau"}
print(my_set)

my_set = set([1, 2, 3, 4, 4])
print(my_set)

my_set = set((1, 2, 3, 4, 4))
print(my_set)

my_set = set("abcdefffgggghhhiii")
print(my_set)

# default {} -> dict
a = {}
print(type(a))

a = set()
print(type(a))

# methods
my_set = set()

my_set.add(1)
my_set.add('a')
my_set.add(True)
my_set.add(False)

print(my_set)

print(set({1,True})) # result is {1}

my_set = {"apple", "banana", "grape", "strawberry"}
# my_set.remove("orange") -> use discard instead
my_set.discard("orange")
print(my_set)
my_set.remove("banana")
print(my_set)
my_set.pop()
print(my_set)

# frozen set
my_set = frozenset([1, 2, 3, 4, 5, 5])
print(my_set)


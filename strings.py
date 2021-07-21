my_string = "Hello world"
print(my_string)

# iterating
for char in my_string:
    print(char, end=" ")
    pass
print()
for i in range(len(my_string)):
    print(my_string[i], end=' ')
    pass
print()

print(my_string.strip())

# not in-place
print(my_string.upper())
print(my_string.lower())
print(my_string)

print(' '.join(['a', 'b', 'c', 'd']))

print(my_string.count('ll'))
print(my_string.count('l'))
print(my_string.find('l'))

# Format
my_string = "Hello {} and {}".format("Tom", "Jerry")
print(my_string)

my_string = "Hello %s and %s" % ("Thomas", "Jeremy")
print(my_string)

# f-string
name = "Tom"
food = "fish"
my_string = f"Hello, my name is {name} and I like {food}"
print(my_string)

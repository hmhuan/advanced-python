import random

# random float in [0, 1)
print(random.random())

# random float in range [a, b]
print(random.uniform(2, 12))

print(random.randrange(1, 10))
# random integer in range [a, b]
print(random.randint(1, 10))

# random float with muy and sigma
print(random.normalvariate(1, 2))

# choose random element from a sequence
print(random.choice([1,3,4, 5, 8, 10]))

print(random.choice(list("acegik")))

# choose k unique (without replacement)
print(random.sample(list("ABCDEFGH"), 5))

# choose k element with replacement and return k sized list
print(random.choices(list("ABCDEFGHI"), k=4))

# shuffle a list
a = list("ABCEDFGHI")
random.shuffle(a)
print(a)

# The seed generator
print('Seeding with 1...\n')

random.seed(1)
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 42...\n')
random.seed(42)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 1...\n')
random.seed(1)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 42...\n')
random.seed(42)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

# secrets module
import secrets

print("--------- SECRETS MODULE --------")
a = secrets.randbelow(10)
print(a)

a = secrets.randbits(10)
print(a)

print(secrets.choice(list("ABCDEFGH")))


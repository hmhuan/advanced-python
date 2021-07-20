my_dict = {"name": "Ming", "age": 21, "city": "New York"}
print(my_dict)

name = my_dict["name"]
print(name)

my_dict["email"] = "abc@gmail.com"
print(my_dict)

# delete key - value
del my_dict["email"]
print(my_dict)

city = my_dict.pop("city")
print(city)
print(my_dict)

print(my_dict.popitem())

# loop in dictionary
my_dict = {"name": "Ming", "age": 21, "city": "New York"}

for key in my_dict:
    print(my_dict[key])
    pass

for value in my_dict.values():
    print(value)
    pass

for key, value in my_dict.items():
    print(key, value)
    pass

# copy a dictionary
new_my_dict = my_dict.copy()
new_my_dict["name"] = "Tokyo"
print(new_my_dict)
print(my_dict)

# merge dictionaries using update()
# existing keys are overwritten, new keys are added
my_dict.update(new_my_dict)
print(my_dict)

# use tuple (immutable) as a key - list cannot because mutable
my_dict = {(1, 2): 1, (2, 3): 0}
print(my_dict)

# nested dictionaries -> should you copy not using pass reference
my_dict_1 = {"name": "Ming", "age": 21, "city": "New York"}
my_dict_2 = {"name": "Tokyo", "age": 22, "city": "Las Vegas"}

nested_dict = {"dict1": my_dict_1, "dict2": my_dict_2}

my_dict_1["name"] = "kanojo"
print(my_dict_1)
nested_dict["dict1"]["name"] = "naruto"
print(my_dict_1)
print(nested_dict)

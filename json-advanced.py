import json

# Serialization / encoding object -> json
person = {'name': 'John', 'age': 30, 'city': 'New York', 'job': ['engineer', 'developer']}

person_json = json.dumps(person)
print(person_json)

person_json_2 = json.dumps(person, indent=4, separators=(";", "="), sort_keys=True)
print(person_json_2)

# save to file using json.dump
with open('person.json', 'w') as f:
    json.dump(person, f)
    pass

# Deserialization json -> object
person_json = """
{
    "age": 30, 
    "city": "New York",
    "hasChildren": false, 
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""

person = json.loads(person_json)
print(person)

with open('person.json', 'r') as f:
    person_2 = json.load(f)
    print(person_2)
    pass

# Custom object
def encode_complex(z):
    if isinstance(z, complex):
        return {z.__class__.__name__: True, "real": z.real, "imag": z.imag}
    else:
        raise TypeError(f"Object of type '{z.__class__.__name__}' is not JSON serializable")

z = 5 + 9j
z_json = json.dumps(z, default=encode_complex)
print(z_json)

from json import JSONEncoder

class ComplexEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(z, complex):
            return {z.__class__.__name__: True, 'real': z.real, 'imag': z.imag}
        
        return super().default(self, o)

z = 5 + 9j
z_json = json.dumps(z, cls=ComplexEncoder)
print(z_json)

# or use
z_json = ComplexEncoder().encode(z)
print(z_json)

# decoding for complex
z_obj = json.loads(z_json)
print(type(z_obj))
print(z_obj)

def decode_complex(z_obj):
    if complex.__name__ in z_obj:
        return complex(z_obj['real'], z_obj['imag'])
    return z_obj
    pass

z = json.loads(z_json, object_hook=decode_complex)
print(type(z))
print(z)

# template for encoding and decoding fucntion
class User:
    def __init__(self, name, age, active, balance, friends):
        self.name = name
        self.age = age
        self.balance = balance
        self.active = active
        self.friends = friends

class Player:
    def __init__(self, name, nickname, level):
        self.name = name
        self.nickname = nickname
        self.level = level
        pass

def encode_obj(obj):
    obj_dict = {
        '__class__': obj.__class__.__name__,
        '__module__': obj.__module__
    }
    
    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)
    
    return obj_dict

def decode_obj(obj_dict):
    obj = None
    if '__class__' in obj_dict:
        class_name = obj_dict.pop('__class__')

        module_name = obj_dict.pop('__module__')

        module = __import__(module_name)

        class_ = getattr(module, class_name)

        obj = class_(**obj_dict)
    else:
        obj = obj_dict
    
    return obj

user = User("Michael", 26, True, balance=10000, friends=["Riot", "Zed", "Yasuo"])

## encode user
user_json = json.dumps(user, default=encode_obj)
print(user_json)

## decode user
user_obj = json.loads(user_json, object_hook=decode_obj)
print(user_obj)


player = Player("Black", "abcxyz", 102)
player_json = json.dumps(player, default=encode_obj)
print(player_json)

player_obj = json.loads(player_json, object_hook=decode_obj)
print(player_obj)



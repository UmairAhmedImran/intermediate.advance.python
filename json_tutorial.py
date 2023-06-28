import json

#person = {"name":"Jhon", "age":30, "city":"New York", "hasChilderen":False, "titles": ["engineer", "programmer"]}

#personJSON = json.dumps(person, indent=4, sort_keys=True)
#print(personJSON)

#with open("person.json", "w") as file:
 #   json.dump(person, file, indent=4)

#person = json.loads(personJSON)
#with open("person.json", "r") as file:
 #   file_person = json.load(file)
  #  print(file_person)

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 30)


def encode_user(x):
    if isinstance(x, User):
        return {'name': x.name, 'age': x.age, x.__class__.__name__: True}
 #   else:
 #       raise TypeError('Object of type User is not JSON serializable')

#userJSON = json.dumps(user, default=encode_user)
#print(userJSON)
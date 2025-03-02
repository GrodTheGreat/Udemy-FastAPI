"""
Function Assignment
- create function that takes 3 parameters
    - firstname
    - lastname
    - age
- returns a dictionary based on those values
"""


def person_factory(firstname, lastname, age):
    new_person = {"firstname": firstname, "lastname": lastname, "age": age}
    return new_person


person = person_factory(firstname="Eric", lastname="Roby", age=32)
print(person)

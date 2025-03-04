"""
- create list of 5 animals called zoo
- delete animal at 3rd index
- append a new animal at the end of the list
- delete the first animal in the list
- print all the animals
- print only the first 3 animals
"""

zoo = ["Lion", "Rhino", "Elephant", "Hyena", "Crocodile"]
# This would pop the 3rd animal in the list, if you want the animal at
# the index of 3 then it's zoo.pop(3)
zoo.pop(2)
zoo.append("Giraffe")
zoo.pop(0)
print(zoo)
print(zoo[0:3])

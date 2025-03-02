"""
Dictionaries
"""

user_dictionary = {"username": "codingwithroby", "name": "Eric", "age": 32}

print(user_dictionary)
print(user_dictionary.get("username"))

user_dictionary["married"] = True
print(user_dictionary)
print(len(user_dictionary))

user_dictionary.pop("age")
print(user_dictionary)

user_dictionary.clear()
print(user_dictionary)

del user_dictionary
# print(user_dictionary) # This will raise an error since it was deleted

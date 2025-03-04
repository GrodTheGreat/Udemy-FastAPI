"""
Sets are similar to lists but are unordered and cannot contain duplicates
Uses curly braces
"""

my_set = {1, 3, 4, 5, 1, 2}
print(my_set)
print(len(my_set))

for x in my_set:
    print(x)

# my_set[0] # This will throw an error

my_set.discard(3)
print(my_set)
my_set.add(6)
print(my_set)
my_set.update([7, 8])
print(my_set)


my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[1])

# Tuples are immutable, they cannot be updated

"""
Lists are a collection of data. (Not to be confused with an array)
"""

my_list = [80, 96, 72, 100, 8]
print(my_list)

people_list = ["Eric", "Adil", "Jeff"]
people_list[0] = "Mel"
print(people_list[-1])
print(len(people_list))
print(people_list[0:2])

my_list.append(1000)
print(my_list)
my_list.insert(2, 1000)
print(my_list)
my_list.remove(8)
print(my_list)
my_list.pop()
print(my_list)
my_list.sort()
print(my_list)

"""
For and While loops
"""

my_list = [1, 2, 3, 4, 5]

# cringe, soy way fo doing this...
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

# based, chad way of doing it...
for iterator in my_list:
    print(iterator)

for i in range(3, 6):
    print(i)

sum = 0
for i in my_list:
    sum += i

print(sum)

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for i in my_list:
    print(f"Happy {i}!")

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now larger or equal to 5")

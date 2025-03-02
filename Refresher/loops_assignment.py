"""
- given: my_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
- create while loop that prints all elements of my_list 3 times
- when printing the elements, use a for loop
- however, continue if element is Monday
"""

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i = 0
while i < 3:
    i += 1
    for day in my_list:
        if day == "Monday":
            continue
        print(day)

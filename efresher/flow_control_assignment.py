"""
- create variable grade holding an integer between 0-100
- code if, elif, else statements to print the letter grade of the number grade variable
- grades:
a = 90-100
b = 80-89
c = 70-79
d = 60-69
f = 0-59 
e.g. if grade = 87 then print('B')
"""

grade = int(input("Enter your grade: "))

if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade >= 70 and grade <= 79:
    print("C")
elif grade >= 60 and grade <= 69:
    print("D")
elif grade >= 0 and grade <= 59:
    print("F")
else:
    print("Error, grade enter is not valid")

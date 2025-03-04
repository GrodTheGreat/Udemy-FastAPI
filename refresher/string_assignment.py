"""
String Assignment we will do together:

Ask the user how many days until their birthday and print an approx
number of weeks until their birthday

Week is = 7 days (lol)
decimals within the return is allowed... (but cringe)
"""

days_left = input("How many days until your birthday? ")
weeks_left = round(int(days_left) / 7)

print(f"There are about {weeks_left} weeks left until your next birthday!")

"""
Functions
"""

print("Welcome to functions!")


def my_function():
    print("Inside the function")


my_function()


def print_my_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")


print_my_name("Eric", "Parker")


def print_color_red():
    color = "Red"
    print(color)


color = "Blue"
print(color)
print_color_red()


def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)


print_numbers(10, 3)
print_numbers(3, 10)


def multiply_numbers(a, b):
    return a * b


solution = multiply_numbers(10, 6)
print(solution)


def print_list(list_of_numbers):
    for item in list_of_numbers:
        print(item)


numbers_list = [1, 2, 3, 4, 5]
print_list(numbers_list)


def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = 0.03
    return cost_of_item * current_tax_rate


final_cost = buy_item(50)
print(final_cost)

# file = open("../files/data.txt", 'w')
#
# file.write("100.12" + '\n')
# file.write("111.23" + '\n')
#
# file.close()


# try:
#     waiting_list = ["john", "marry"]
#     name = input("Enter name: ")
#
#     number = waiting_list.index(name)
#     print(f"{name}'s turn is {number}")
#
# except ValueError:
#     print(f"{name} is not in the list")

# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     print(maximum)
#     return maximum
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)

# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
#
#
# time = calculate_time(123)
# print(time)

from parsers import parse
import random

# Ask the user to enter a lower and an upper bound divided by a comma
user_input = input("Enter a lower bound and an upper bound divided a comma (e.g., 2,10)")

# Parse the user string by calling the parse function
parsed = parse(user_input)

# Pick a random int between the two numbers
rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])

print(rand)
# list comprehension
numbers = [1, 2, 3]
new_numbers = [num + 1 for num in numbers]
print(new_numbers)  # [2, 3, 4]


name = "John"
letters_list = [letter for letter in name]
print(letters_list)  # ['J', 'o', 'h', 'n']

duble_num_list = [num * 2 for num in range(1, 5)]
print(duble_num_list)  # [2, 4, 6, 8]


# conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Joe", "Freddie"]

short_names = [name for name in names if len(name) < 5]
print(short_names)  # ['Alex', 'Beth', 'Dave', 'Joe]

long_caps_names = [name.upper() for name in names if len(name) > 5]
print(long_caps_names)  # ['CAROLINE', 'ELEANOR', 'FREDDIE']


# exercices
# 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [num * num for num in numbers]

# Write your code 👆 above:

print(squared_numbers)


# 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above
# This new list should only contain the even numbers from the list numbers
# Write your 1 line code 👇 below:

result = [num for num in numbers if num % 2 == 0]

# Write your code 👆 above:

print(result)


# 3
"""Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.
"""

with open("file1.txt") as data:
    numbers1 = list(data.read().split("\n"))
    # numbers1 = data.readlines()

with open("file2.txt") as data:
    numbers2 = list(data.read().split("\n"))
    # numbers2 = data.readlines()


result = [int(item)
          for item in numbers1 if item in numbers2]


# Write your code above 👆

print(result)

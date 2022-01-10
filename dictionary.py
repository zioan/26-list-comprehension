# dictionary comprehension
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Joe", "Freddie"]
score = {student: random.randint(1, 10) for student in names}

print(score)
# {'Alex': 1, 'Beth': 10, 'Caroline': 8, 'Dave': 8, 'Eleanor': 9, 'Joe': 8, 'Freddie': 1}

#########################

students = {'Alex': 1, 'Beth': 10, 'Caroline': 4,
            'Dave': 8, 'Eleanor': 7, 'Joe': 5, 'Freddie': 1}

passed_students = {key: value for (
    key, value) in students.items() if value > 5}
# Or
passed_students = {student: score for (
    student, score) in students.items() if score > 5}

print(passed_students)


# Exercices
# 1
"""You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop."""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {item: len(item) for item in sentence.split()}

# print(sentence_list)
print(result)


# 2
"""You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
"""
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:


weather_f = {day: value * 9/5 + 32 for (day, value) in weather_c.items()}

print(weather_f)

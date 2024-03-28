# Day 1

# How old are you?
# user responds with age
# f"You are {age} years old"
question = input("How old are you? ")
print(f"You are {question} years old. ")

# Number of days - 365
# Number of weeks - 52
# Number of months - 12
# print("fThe number of years is {}")
# Create variables for days, weeks, months
# multiply days, weeks, months with perminater
def b_day(x):
    days = 365
    weeks = 52
    months = 12

    print(f"In {x} years is {x * days} days, {x * weeks} weeks, and {x * months} months.")
b_day(14)

# Day 2

question1 = input("What is your name? ")
question2 = input("How old are you? ")
print(f"Your name is {question1} and you are {question2} years old")

# In this exercise for day 2, it states that I need to correct any issues in the code below:
"""
hourly_wage = input("Please enter your hourly wage: ')

prnt("Hourly wage: ")
print(hourlywage)
print("Hours worked: ")
print(hours_worked)

hours_worked = input("How many hours did you work this week? ")
"""

# Here is the corrected code:
hourly_wage = input("Please enter your hourly wage: ")

print("Hourly wage: ")
print(hourly_wage)
print("Hours worked: ")
hours_worked = input("How many hours did you work this week? ")
print(hours_worked)

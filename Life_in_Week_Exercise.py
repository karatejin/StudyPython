# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.
# e.g. When you hit run, this is what should happen:

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 1year

x = 365 #days

y = 52 #weeks

z = 12 #month

# 90 year
# it add with input age

new_x = (x * 90) - (x * int(age))

new_y = (y * 90) - (y * int(age))

new_z = (z * 90) - (z * int(age))

# show remain life in 90 year

print(f"you have {new_x}days , {new_y} weeks , and {new_z} months left.")


# 다른 스타일로 풀기
# age_as_int = int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining *365
# weeks_remaining = years_remaining*52
# months_remaining = years_remaining*12

# print(f"You have {days_remaining} days, {weeks_remaining}weeks, and {months_remaining}days")
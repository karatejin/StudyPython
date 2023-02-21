
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_weight = float(weight)
new_height = float(height)

BMI = round(new_weight/(new_height**2))

result = BMI

if result < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif result < 25:
    print(f"Your BMI is {result}, you have a normalweight.")
elif result < 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif result < 35:
    print(f"Your BMI is {result}, you are obese")
else:
    print(f"Your BMI is{result}, you are clinically obese")
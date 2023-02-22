#윤년

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0 or year % 100 !=0 and year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year")


## or 또는 and 없이 코드를 짠다면?

if year % 4 == 0:
    print("Leap year.")
elif year % 100 == 0:
    print("Not leap year.")
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")

# 다른 풀이

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year")
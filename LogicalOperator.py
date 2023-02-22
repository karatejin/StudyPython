# 논리 연산자

# and = 코드 전체에서 둘다 True이어야 한다 둘중 하나라도 False이면 False이다.
# or = 둘중 하나라도 True이면 True이다. 모두 False이면 False이다.
# not = 조건의 반대로 결과를 만든다. 조건이 False이면 결과는 True/ 조건이 True이면 결과는 False

# if Customers are midlife crisis will provide for free
# midlife cirsis happen typically 44 to 55 years old

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
####################################################
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <=18:
        bill = 7
        print("Youth tickets are is $ 7")
    elif age <= 55 and age >= 45:
        print("Everything is going on to be ok. Have a ride on us!!")
    else:
        bill =12
        print("Adult tickets are $12")
    

    wants_photo = input("Do you want a photo take? Y or N. ")
    if wants_photo == "Y":
        bill +=3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
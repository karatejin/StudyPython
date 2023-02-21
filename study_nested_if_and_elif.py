# 중첩 if문과 elif 문
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
####################################################
if height >= 153:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Your pay is $5")
    elif age <=18:
        print("Your pay is $ 7")
    else:
        print("Your pay is $12")
else:
    print("Sorry, you have to grow taller before you can ride.")

#만약에 주니어 코스터 라면??

print("주니어 코스터에 오신것을 환영합니다!")
height = int(input("키가 몇 cm 이실까요?? "))

if height <= 153:
    print("어서 오세요 어린이 여러분!")
    age = int(input("손님 나이가 몇살이에요? "))
    if age < 4:
        print("우리 내년에 봐요!")
    elif age <= 13:
        print("10000원 입니다!")
    elif age <= 20:
        print("저기 T익스프레스를 이용해 주세요!")
    else:
        print("보호자는 밖에서 대기해 주세요!")
else:
    print("여기서 이러시면 안됩니다!")

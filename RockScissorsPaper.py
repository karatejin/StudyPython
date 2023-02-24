## 가위 바위 보
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("가위 바위 보 게임을 시작합니다. (숫자를 입력해주세요) : 0.바위 1.가위, 2.보 \n 당신의 선택은??: "))

if choice == 0 :
    print("당신의 선택은 : " + rock)

elif choice == 1:
    print("당신의 선택은 : " + scissors)

elif choice == 2:
    print("당신의 선택은 : " + paper)

##=======

## 컴퓨터 선택

map = [rock,scissors,paper]


computer_choice = random.randint(0,2)

if computer_choice == 0:
    print("컴퓨터의 선택은 : " + map[0])
elif computer_choice ==1:
    print("컴퓨터의 선택은 : " + map[1])
elif computer_choice ==2:
    print("컴퓨터의 선택은 : " + map[2])

## 승부

if choice == computer_choice:
    print("무승부")
elif choice != computer_choice:
    if choice == 0 and computer_choice == 1 :
        print ("당신의 승리")
    elif choice == 1 and computer_choice == 2 :
        print("당신의 승리")
    elif choice == 2 and computer_choice == 0 :
        print("당신의 승리")
    elif choice > 2 or choice < 0:
        print("잘못된 숫자 입력 당신의 패배!!")
    else:
        print("당신의 패배")

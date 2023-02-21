#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("팁 계산기를 이용해 주셔서 감사합니다.")

bill = float(input("총 지불할 금액은? $"))

tip_percent = float(input("팁은 어느정도 생각하세요? 10, 12 또는 15? ")) * float(1/100)

split_people = float(input("같이 식사를 즐긴 인원은 몇명이세요? "))

pay_per_person = round((bill/split_people)+((bill/split_people)*tip_percent), 2)

result = "{:.2f}".format(pay_per_person) #소수점 두번째 자리가 0이어도 보이게 하기

print(f"각 인원당 지불 하실 금액은: ${result}")


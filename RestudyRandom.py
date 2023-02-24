# 임의의 개수로 이름을 넣고 무작위 로 하나의 결과를 보여주기

import random

#이름 작성
names_stirng = input("이름을 작성해주세요, 쉼표와 띄어쓰기를 합시다. : ")

names = names_stirng.split(", ") ## 스플릿 지정


# 랜덤 결과 보여주기

names_item = len(names)

random_choice = random.randint(0, names_item-1)

who_is_result = names[random_choice]

print(who_is_result)
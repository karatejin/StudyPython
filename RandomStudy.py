import random

random_integer = random.randint(1, 10) #randint는 정수 지정한 범위내 두개의 값을 정해줘라
print(random_integer)

random_float = random.random() * 5 # random.random() 괄호안에 no args 은 1 이내의 소수점 1은 출력 안함
print(random_float)

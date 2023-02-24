# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ") ##-- 문자열을 쪼개준다
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# num_items = len(names) ##-- 각 이름 목록의 길이 

# random_choice = random.randint(0, num_items-1) ##-- 처음 부터 끝까지. num_items -1을 한 이유는 len(names) 에서 4을 출력한다.(이름이 4개일때) 하지만 배열에선 0 부터 3이기 때문에 -1을 해준다.

# who_pay_all = names[random_choice]

who_pay_all = random.choice(names)

print(who_pay_all + " is going to buy the meal today!")





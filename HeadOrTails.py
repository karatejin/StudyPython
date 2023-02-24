import random
#Remember to use the random module -- 랜덤 모듈을 써라.
#Hint: Remember to import the random module here at the top of the file. 🎲 import Random 을 해라

#Write the rest of your code below this line 👇

#print("Heads or Tails? : ") ##--있어도 없어도 되는것 문제에서는 요구하지 않음.

Head_or_Tails = random.randint(0,1)

if Head_or_Tails == 0:
    print("Heads")

else:
    print("Tails")


print(Head_or_Tails)


## 행맨

## 무작위로 단어 고르고 정답확인
import random

word_list =["ardvark","baboon","camel","dragon"]

## test code

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Enter your guess: ").lower()

for letter in chosen_word:
    if  letter == guess:
        print("Right")
    else:
        print("Wrong")

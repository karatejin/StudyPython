## 행맨

## 빈칸을 맞춘 글자로 바꾸기
import random

word_list =["ardvark","baboon","camel","dragon"]

## test code

chosen_word = random.choice(word_list)
print(f"select word is : {chosen_word}")

display = []
word_length = len(chosen_word)


for _ in range(word_length):
    display += "_"
print(display)

guess = input("Enter your guess: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if  letter == guess:
        display[position] = letter
print(display)

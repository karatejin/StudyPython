## 행맨

## 빈칸을 맞춘 글자로 바꾸기
import random
import hangman_art
# import hangman_words
import os


print(hangman_art.logo)

## -- hangman_words import -- ##

from hangman_words import word_list

chosen_word = random.choice(word_list)

lives = 6

##--- 글자의 개수 보여주기
display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Enter your guess: ").lower()
    os.system("cls")
    

    ## -- 유저가 이미 입력한 글자가 있다면 알려주기
    if guess in display:
        print("You have already guessed that letter")

    ## -- 컴퓨터가 선택한 글자
    for position in range(word_length):
        letter = chosen_word[position]

        ## -- 플레이어가 추측한 글자와 컴퓨터가 선택한 글자가 일치하면 출력해서 보여주기
        if letter == guess:
            display[position] = letter

    ## -- 컴퓨터가 선택한 글자와 플레이어가 추측한 글자가 일치 하지 않으면 남은 lives 를 감소
    if guess not in chosen_word:
        print(f"you guess {guess} is not in the word you lose your life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose!! answer is {chosen_word}")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(hangman_art.stages[lives])
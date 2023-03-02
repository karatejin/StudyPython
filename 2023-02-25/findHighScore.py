## max() 함수를 쓰지 말것
## min() 함수도 쓰지 말것

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# max_number = student_scores[0]

# for number in student_scores[1:]: ## student_scores[1:] 를쓰는 이유 student_scores[0]이 초기값에 할당 되었기 때문에 [1] 번째 부터 모든 요소를 포함하는 새목록을 만든다.
#     if number > max_number:
#         max_number = number
# print(f"The highest score in the class is : {max_number}")

####################

hightest_score = 0
for score in student_scores:
    if score > hightest_score:
        hightest_score = score
print(hightest_score)
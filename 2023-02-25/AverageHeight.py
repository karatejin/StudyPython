### for 문을 통한 평균 구하기

## len(), sum() 을 사용하지 말것

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0

for height in student_heights:
  total_height += height
print(total_height)

number_of_students = 0

for student in student_heights:  
  number_of_students += 1
print(number_of_students)

avg = round(total_height/number_of_students)
print(avg)
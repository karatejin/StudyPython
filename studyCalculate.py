# 기본 연산

3 + 5 # 더하기
7 - 4 # 빼기
3 * 2 # 곱하기
6 / 3 #나누기
2 ** 2 # 제곱

# print(2**3)
# print (type(6/3))

#PEMDAS #연산 순서
# () Parentheses 괄호
# ** Exponents  지수
# *  Multiplication 곱셉  곱셉과 나눗셈중 가장 왼쪽에서 부터 연산을 처리함
# /  Division   나눗셈
# +  Addition   덧셈
# -  Subtraction    

# print(3 * 3 + 3 / 3 - 3)

# 위의 식을 이용해 결과값이 3이 되게 하시오.

# print(3 * (3 + 3) / 3 - 3)


# 반올림

# print(round(8/3)) # 그냥 반올림

# print(round(8/3 ,2)) #소수 두번째 자리까지 반올림한다.


# 버림

# print(8//3)


###################
# result = 4/2
# result /= 2

# print (result)

# score = 0

# # User scores a point

# # score += 1

# # print(score)

# print("당신의 점수는 " + str(score))

#####################
# 복합적으로 출력하기

score = 0   #integer
height = 1.8    #float
isWinning = True    #Boolean

# print("당신의 점수는" + str(score) + "당신의 키는 " + str(height) + " 이기고 있나?" + str(isWinning))

# # f-String
print(f"당신의 점수는? {score} , 당신의 키는 {height} , 당신은 이기고 있나요?{isWinning}")

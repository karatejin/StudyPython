#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.πͺ

#Write your code below this line π

print("ν κ³μ°κΈ°λ₯Ό μ΄μ©ν΄ μ£Όμμ κ°μ¬ν©λλ€.")

bill = float(input("μ΄ μ§λΆν  κΈμ‘μ? $"))

tip_percent = float(input("νμ μ΄λμ λ μκ°νμΈμ? 10, 12 λλ 15? ")) * float(1/100)

split_people = float(input("κ°μ΄ μμ¬λ₯Ό μ¦κΈ΄ μΈμμ λͺλͺμ΄μΈμ? "))

pay_per_person = round((bill/split_people)+((bill/split_people)*tip_percent), 2)

result = "{:.2f}".format(pay_per_person) #μμμ  λλ²μ§Έ μλ¦¬κ° 0μ΄μ΄λ λ³΄μ΄κ² νκΈ°

print(f"κ° μΈμλΉ μ§λΆ νμ€ κΈμ‘μ: ${result}")


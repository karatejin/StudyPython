# 🚨 Don't change the code below 👇
row1 = ["⬜️️","⬜️️","⬜️️"]
row2 = ["⬜️️","⬜️️","⬜️️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0]) ## position 입력값의 첫번째 int
vertical = int(position[1]) ## position 입력값의 두번째 int

map [vertical-1][horizontal-1] = "✨"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
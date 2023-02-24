##---- list study

province_of_korea = ["경상남도","경상북도","전라남도","전라북도","제주특별자치도","강원도","충청남도","충청북도","경기도"] ##--대괄호 안에 작성
metropolitan_korea =["부산광역시","대구광역시","광주광역시","울산광역시","통합창원시","대전광역시","세종특별자치시","수원특례시","고양특례시","용인특례시"]

# print(province_of_korea[0]) ##-- 대괄호안 숫자를 입력하면 각 변수의 순서에 따라 출력
# print(metropolitan_korea[-1]) ## -1을 입력하면 배열의 마지막 순서가 출력 , 인덱스는 양수 음수 모두 가능하다.

# metropolitan_korea[4] = "창원특례시"
# print(metropolitan_korea)

province_of_korea.append("김해시")
print(province_of_korea)
##---- index Error 중첩리스트

province_of_korea = ["경상남도","경상북도","전라남도","전라북도","제주특별자치도","강원도","충청남도","충청북도","경기도"]
metropolitan_korea =["부산광역시","대구광역시","광주광역시","울산광역시","통합창원시","대전광역시","세종특별자치시","수원특례시","고양특례시","용인특례시"]

# num_of_provice = len(province_of_korea)

# print(num_of_provice)

# print(province_of_korea[num_of_provice-1])
# print(metropolitan_korea[10])

## 중첩 리스트

region_of_korea = [province_of_korea,metropolitan_korea]

print(region_of_korea[1][1]) ##== region_of_korea 의 [1] 번째 배열(metropolitan)의 [1]번 째 배열
# 변수 
# 1.변수이름 = 데이터
# 2. 데이터를 저장할 공간
# 3. 언제든지 데이터를 변경할수 있다.
# 4. 규칙
#    - 데이터를 표현할수 잇는 이름으로 짓는다.
#    - 문자부터 시작해야 한다.
#    - 대소문자는 구분한다.
#    - _ 로 시작할수 있다.
#    - 미리 예약된 키워드는 사용할수 없다.

# 마스터이 챔피언 데이터를 변수에 저장
name = "마스터이"
level = 5
health = 800
attack = 90
print(name, level, health, attack)

# 변수에 저장된 데이터를 변경하기
level = level + 1
health = health + 50
attack = attack + 10

print(name, level, health, attack)
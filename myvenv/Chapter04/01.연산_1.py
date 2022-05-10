# 연산
# 1. 수나 식을 일정한 규칙에 따라 계산하는 것
# 2. 종류
#   - 대입연산
#       1. 변수 이름 = 데이터
#   - 산술연산
#        1. 숫자연산
#           +(더하기), -(빼기), *(곱하기), /(나누기), //(몫), %(나머지), **(제곱)
x = 5
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

#        2. 문자열 연산
tag1 = "#내꺼하자"
tag2 = "#오늘부터1일"
tag3 = "#여친생김"

tag = tag1 + tag2 + tag3
print(tag)

message = "우린 모두 파이썬을 사랑합니다.\n" * 5
print(message)

#       3. 복합 할당 연산자
level = 10 # (레벨 1 증가)
level += 1 # level = level + 1
health = 2000 # (체력이 300 감소)
health -= 300 # health = health - 300
attack = 300 #(공격력 1.5배 증가)
attack *= 1.5 # attack = attack * 1.5
speed = 420 # (이동속도 50% 감소)
speed /=2 # speed = speed / 2

print(level, health, attack, speed)

#   - 비교연산
#   - 논리연산
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
print("=======================================================")
#        2. 문자열 연산
tag1 = "#내꺼하자"
tag2 = "#오늘부터1일"
tag3 = "#여친생김"

tag = tag1 + tag2 + tag3
print(tag)

message = "우린 모두 파이썬을 사랑합니다.\n" * 5
print(message)
print("=======================================================")
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
print("=======================================================")
#   - 비교연산
#       >(크다), <(작다), >=(크거나 같다), <=(작거나 같다), ==(같다), !=(다르다)
print(2 > 3)   # False
print(15 < 30)  # True
print(1.5 >= 0) # True
print(3 <= 3) # True
print("팙팗팚" == "팙팗팗") # False
print("1111111111111111111" != "1111111111111111111") # False
print("1111111111111111111" == 1111111111111111111) # False
print("=======================================================")
#   - 논리연산
#       A and B (A,B 모두 참이면 True), A or B ( A,B중 하나라도 참이라면 True), not A (A가 참이라면 False)
print(4 < 6 and 10 >= 10)  # True
print("포기하지말아요" != "포기하지말아요" or "나는 할 수 있다" == "나는 할 수 있다")  # True
print(not 5==5) # False
print("=======================================================")
#   - 멤버십 연산
#     in(포함되어 있다), not in (포함되어 있지 않다)
print("a" in "abc") # 포함되어 있다면 True
print("d" not in "abc") # 포함되어 있지 않다면 True

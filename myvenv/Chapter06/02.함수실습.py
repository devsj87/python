# 기본형
# 정의 하기
def printHello():
    print("Hello")

# 호출
printHello()

# 매개변수가 있는 함수
def sum(a,b):
    print(a+b)

# 호출
sum(1,2)

# 반환값이 있는 함수
import random
def getRandomNumber():
    number = random.randint(1,10)
    return number

# 호출
print(getRandomNumber())

# 매개변수와 반화값이 있는 함수
def add(a,b):
    result = a + b
    return result
# 호출
print(add(5,6))
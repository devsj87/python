# 실습문제 4.3.2
# 사용자로부터 태어난 연도를 입력 받으면
# 현재 나이를 출력하기

from datetime import datetime

current = datetime.today().year
year = int(input("태어난 연도를 입력하세요 >>> "))

print("현재 나이는", current - year + 1, "세 입니다.")


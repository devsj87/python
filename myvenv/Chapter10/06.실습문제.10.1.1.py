# 오류 해결 과정 중심!!!

# 실습문제 10.1.1
# 보유한 주식이 목표가에 도달했을 때의 종목별 수익금과 수익률을 출력해주는 프로그램을 작성해보자
# mystock.csv파일로 부터 종목 매입가, 수량, 목표가 정보를 가져온다.

# 수익금 = (목표가 - 매입가) * 수량
# 수익률 = (목표가 / 매입가 - 1) * 100

import csv

# data = [
#   ["종목", "매입가", "수량", "목표가"],
#   ["삼성전자", 85000, 10, 90000],
#   ["NAVER", 38000, 5, 400000]
# ]
# 파일 쓰기
# with open("./myvenv/Chapter10/mystock.csv", "w") as file:
#   writer = csv.writer(file)
#   for row in data:
#     writer.writerow(row)


def show_profit(data):
  name = data[0] # 종목
  purchase_price = int(data[1]) # 매입가
  amount = int(data[2]) # 술향
  target_price = int(data[3]) # 목표가

  profit = (target_price - purchase_price ) * 100 # 수익금
  profit_ratio = (target_price / purchase_price -1) * 100 # 수익률

  print(f"{name} {profit} {profit_ratio:.2f}%")


# 파일 열기    
file = open("./myvenv/Chapter10/mystock.csv", "r")
reader = list(csv.reader(file))

for data in reader[1:]:
  show_profit(data)

file.close()


# with open("./myvenv/Chapter10/mystock.csv", "r") as file:
#   reader = csv.reader(file)
#   for row in reader:
#     for value in row:
#       print(f"수익금: {( int(value[3]) - int(value[1]) ) * 100}")
#       print(f"수익률: {( int(value[3]) / int(value[1]) -1) * 100}")
  



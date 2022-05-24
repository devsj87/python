# 실습문제 5.2.2
# 턱걸이 평균 측정 프로그램을 만들어보자. 먼저, 턱걸이 횟수를 저장할 빈 리스트를 만든다.
# 그리고 일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장한다. 리스트에 저장된 데이터의 평균을 구해 출력한다

empty = []
a = int(input("1일차 턱걸이 횟수 >>>>"))
b = int(input("2일차 턱걸이 횟수 >>>>"))
c = int(input("3일차 턱걸이 횟수 >>>>"))
d = int(input("4일차 턱걸이 횟수 >>>>"))
e = int(input("5일차 턱걸이 횟수 >>>>"))
f = int(input("6일차 턱걸이 횟수 >>>>"))
g = int(input("7일차 턱걸이 횟수 >>>>"))

empty.append(a)
empty.append(b)
empty.append(c)
empty.append(d)
empty.append(e)
empty.append(f)
empty.append(g)

avg = (a + b + c + d + e + f + g)/7

print(empty)
print(int(avg))

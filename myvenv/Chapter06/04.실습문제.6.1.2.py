# 실습문제 6.1.2
# 다음은 세개의 정수를 인자로 받아, 합계와 평균을 출력해주는 함수이다. 함수를 호출한 결과로 표준 출력이 나오도록 함수를 정의해보자.

# 문자열 포맷팅
def printSumAvg(x,y,z):
  """
  세개의 숫자를 받아 합계와 평균을 출력하는 함수
  """
  sum = x+y+z
  avg = int(sum/3)
  
  print("합계:", sum, "평균:", avg)
  print(f"합계: {sum} 평균: {avg}")

printSumAvg(10,20,30)
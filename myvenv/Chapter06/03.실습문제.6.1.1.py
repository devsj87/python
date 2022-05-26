# 실습문제 6.1.1
# 다음은 두수의 곱셈을 반환하는 multiply 함수이다. multiply 함수를 호출하는 방법으로 옳은것을 고르세요

# docstring : 설명문

def multiply(x,y):
  """
  두수의 곱셈 결과를 반환하는 함수
  매개변수 x : int
  매개변수 y : int
  """
  result = x*y
  return result

multiply(3,5)
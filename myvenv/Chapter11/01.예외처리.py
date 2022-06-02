# 원화를 입력, 환률 입력 -> 달러값

won = input("원화 금액을 입력하세요 >>> ")
dollar = input("환율을 입력하세요. >>> ")

try: # 예외가 발생 할수 있는 코드
    print( int(won) / int(dollar ))
except ValueError as e: # 예외가 발생했을때 실행하는 코드
    print('예외가 발생했습니다.', e)
except ZeroDivisionError as e: 
    print('나누기 0은 불가능 합니다.', e)
else: # 예외가 발생하지 않았을때
    print('예외가 발생하지 않습니다.')
finally: # 항상 실행되는 코드
    print('예외가 발생하던지 발생하지 않던지 항상 실행')
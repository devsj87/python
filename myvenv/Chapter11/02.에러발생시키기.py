# raise 구문을 사용해서 에러를 강제로 발생시켜 봅시다.

try:
    num = int(input('음수를 입력해주세요 >>>'))
    if num > 0 :
        #raise Exception('양수는 입력불가')
        raise ValueError('양수는 입력불가')
#except Exception as e:
except ValueError as e:
    print('에러 발생:', e)

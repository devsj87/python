# 실습문제 5.1.4
# 프로그램 사용자로부터 국어, 수학, 영어 성적이 입력된다. 세 과목의 편균점수가 80점 이상이면 합격이다.
# 그런데 점수에 따라 합격 또는 불합격이 정해지는 프로그램에 오류가 발생했다. 80점 이상일 경우 불합격이 
# 표시되도록 프로그램을 작성해보자. (단, 0점 에서 100점 사이의 숫자를 입력하지 않으면 "잘못 입력하였습니다." 를 출력하자)

ko = int(input('국어 >>> '))
en = int(input('영어 >>> '))
ci = int(input('수학 >>> '))

avg = int((ko + en + ci) / 3)

if avg >=0 and avg <= 100:
    if avg >= 80:
        print("불합격")
    elif avg < 80:
        print("합격")
else:
    print('잘못 입력하였습니다.')

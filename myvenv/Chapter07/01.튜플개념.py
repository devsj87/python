# 튜플
# : 읽기 전용 리스트

a = (3,4,5)
b = 3,4,5

# 한개만 넣을때는 뒤에 , 붙여야한다.
# 한개만 넣을때는 뒤에 , 붙여주지 않으면 int 형으로 저장됨.
c = (3,) 
d = 3,

e = tuple([3,4,5])
f = list(range(10))
g = tuple(f)

i = list(b)

# 튜플 관련 함수
x = 5,6,7
print(max(x))
print(min(x))
print(sum(x))
print(x.count(6))
print(x.index(7))
print(type(x))

print(end="\n\n")

# 리스트도 튜플 관련 함수 사용 가능
print(max(i))
print(min(i))
print(sum(i))
print(i.count(5))
print(i.index(4))
print(type(i))


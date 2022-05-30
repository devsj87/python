# 클래스를 사용하는 이유

champion01_name = "이즈리얼"
champion01_health = 700
champion01_attack = 90

print(f"{champion01_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion02_name = "리신"
champion02_health = 800
champion02_attack = 95

print(f"{champion02_name}님 소환사의 협곡에 오신것을 환영합니다.")

def basic_attack(name, attack):
  print(f"{name} 기본공격 {attack}")


basic_attack(champion01_name, champion01_attack)
basic_attack(champion02_name, champion02_attack)

print("============ 클래스를 사용한 경우 ================")

class Champion:
  def __init__(self, name, health, attack):
    self.name = name
    self.health = health
    self.attack = attack
    print(f"{name}님 소환사의 협곡에 오신것을 환영합니다.")

  def basic_attack(self):
    print(f"{self.name} 기본공격{self.attack}")

ezreal = Champion("이즈리얼", 700, 90)
leesin = Champion("리신",800, 95)
yasuo = Champion("야스오",800, 95)
ezreal.basic_attack()
leesin.basic_attack()
yasuo.basic_attack()
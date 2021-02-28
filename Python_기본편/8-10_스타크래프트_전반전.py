from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} has been summoned".format(name))

    def move(self, location):
        print("{0}: move to {1} [Speed {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0}: {1} damage taken.".format(self.name, damage))
        self.hp -= damage
        print("{0}: Current health is {1}.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: Unit destroyed.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0}: Attack the enemy at {1} [Damage {2}]"\
            .format(self.name, location, self.damage))
    
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)

    # 스팀팩: 일정 시간 동안 이동 및 공격 속도 증가, 체력 10 소모
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0}: Use stimpack. (hp 10 decrease)".format(self.name))
        else:
            print("{0}: Health is lower than 10. Cannot use stimpack".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정, 더 높은 파워로 공격 가능
    seize_developed = False # 시즈모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self)    :
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈모드가 아닐 떄 -> 시즈모드
        if self.seize_mode == False:
            print("{0}: Enable seize mode.".format(self.name))
            self.seize_mode = True
            self.damage *= 2
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0}: Disable seize mode.".format(self.name))
            self.seize_mode = False
            self.damage /= 2

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}: Fly to {1}. [Speed {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, flying_speed, damage):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 5, 20)
        self.cloaked = False # 클로킹 모드 (해제 상태)

    def cloaking(self):
        # 클로킹 모드 -> 모드 해제
        if self.cloaked == True:
            print("{0}: Disable cloaking.".format(self.name))
            self.cloaked = False
        # 클로킹 모드 해제 -> 모드 설정
        else:
            print("{0}: Enable cloaking.".format(self.name))
            self.cloaked = True

def game_start():
    print("[Notification] Starting new game.")

def game_over():
    print("Player: gg")
    print("[Player] left the game.")

# 실제 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1 o'clock")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[Notification] Tank seize mode has been developed.")

# 공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.cloaking()

# 전군 공격
for unit in attack_units:
    unit.attack("1 o'clock")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5 ~ 20)

# 게임 종료
game_over()

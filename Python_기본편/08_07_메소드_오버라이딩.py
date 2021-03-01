# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[Ground Unit Move]")
        print("{0}: move to {1} [Speed {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0}: Attack the enemy at {1} [Damage {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0}: {1} damage taken.".format(self.name, damage))
        self.hp -= damage
        print("{0}: Current health is {1}.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: Unit destroyed.".format(self.name))

# 드랍쉽: 공중 유닛, 수송기, 마린/파이어뱃/탱크 등을 수송, 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}: Fly to {1}. [Speed {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[Flyable Unit Move]")
        self.fly(self.name, location)

# 벌쳐: 지상 유닛, 기동성이 좋음
vulture = AttackUnit("Vulture", 80, 10, 20)

# 배틀크루저: 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("Battle Cruiser", 500, 25, 3)

vulture.move("11 o'clock")
battlecruiser.move("9 o'clock")

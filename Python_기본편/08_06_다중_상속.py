# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
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
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("Valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3 o'clock")

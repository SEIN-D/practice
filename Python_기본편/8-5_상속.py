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
# 메딕: 의무병

# 파이어뱃: 공격 유닛, 화염방사기
firebat1 = AttackUnit("FireBat", 50, 16)
firebat1.attack("5 o'clock")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

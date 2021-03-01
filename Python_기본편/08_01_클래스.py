# # 마린: 공격 유닛, 군인. 총을 쏠 수 있음

# name = "Marine" # unit name
# hp = 40 # unit health
# damage = 5 # unit damage

# print("{0} has been summoned.".format(name))
# print("Health {0}, Damage {1}\n".format(hp, damage))

# # 탱크: 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "Tank"
# tank_hp = 150
# tank_damage = 35

# print("{0} has been summoned.".format(tank_name))
# print("Health {0}, Damage {1}\n".format(tank_hp, tank_damage))

# tank2_name = "Tank"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} has been summoned.".format(tank2_name))
# print("Health {0}, Damage {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0}: Attack the enemy at {1}. [Damage {2}]".format(name, location, damage))

# attack(name, "1 o'clock", damage)
# attack(tank_name, "1 o'clock", tank_damage)
# attack(tank_name, "1 o'clock", tank2_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} has been summoned.".format(self.name))
        print("Health {0}, Damage {1}".format(self.hp, self.damage))

marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank = Unit("Tank", 150, 35)

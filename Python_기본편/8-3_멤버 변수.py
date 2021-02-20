class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} has been summoned.".format(self.name))
        print("Health {0}, Damage {1}".format(self.hp, self.damage))

# marine1 = Unit("Marine", 40, 5)
# marine2 = Unit("Marine", 40, 5)
# tank = Unit("Tank", 150, 35)

# 레이스: 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("Wraith", 80, 5)
print("Name: {0}, Damage: {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤: 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("stolen wraith", 80, 5)
wraith2.cloaking = True

if wraith2.cloaking == True:
    print("{0} is now cloaking.".format(wraith2.name))

class Unit:
    def __init__(self, name, hp, damage): # __init__: 연산자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} has been summoned.".format(self.name))
        print("Health {0}, Damage {1}".format(self.hp, self.damage))

# marine1 = Unit("Marine", 40, 5) # marine, tank: 인스턴스
# marine2 = Unit("Marine", 40, 5)
# tank = Unit("Tank", 150, 35)
marine3 = Unit("Marine")
marine4 = Unit("Marine", 40)

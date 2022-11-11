class Hero:
    Head = 1
    Ability = True
    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage
    def heal(self):
        print(self.hp + 100)
    def two_damage(self):
        print(self.damage * 2)
    def greeting(self):
        print(f'my name is {self.name}')
    def brand_phrase(self):
        print('good will win')
h1 = Hero(name = 'Elprimo', nickname = 'Primas', hp = 810, damage = 200 )
h2 = Hero(name = 'Edgar', nickname = 'Nefor',hp = 450, damage = 120 )
h3 = Hero(name = 'Mortis', nickname = 'Matras', hp = 540, damage = 102)
h4 = Hero(name = 'Frank', nickname = 'Zombie', hp = 945, damage = 167)
class Heroaqua(Hero):
    jabry = 6
    def __init__(self, name, nickname, hp, damage, fly = False):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage
        self.fly=fly
    def brand_phrase(self):
        fly = True
        print('fly in the True phrase')
    def Gen_x(self):
        pass
class Heroair(Hero):
    wings = 2
    def __init__(self, name, nickname, hp, damage,fly = False):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage
        self.fly = fly
    def brand_phrase(self):
        fly = True
        print('fly in the True phrase')
    def Gen_x(self):
        pass
class Herocosmo(Hero):
    airbaloon = 2
    def __init__(self, name, nickname, hp, damage, fly = False):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage
        self.fly = fly
    def brand_phrase(self):
        fly = True
        print('fly in the True phrase')
    def Gen_x(self):
        pass
air = Heroair('bird', 'ptichka', 200, 50)
aqua = Heroaqua('fish','ryba', 250, 100)
cosmo = Herocosmo('astro', 'cosm', 450, 250)
air.brand_phrase()
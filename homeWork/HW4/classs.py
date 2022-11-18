class Hero():
    def __init__(self,name, ability):
        self.name = name
        self.ability = ability
class Hero_Super(Hero):
    def __str__(self):
        return f'{self.name} it is super_hero'
    def deviz(self):
        print(f'{self}')
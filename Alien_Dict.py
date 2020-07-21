import random
playerHP = random.randint(300, 500)
alienHP = random.randint(250, 900)

class alienDefinition():
    def __init__(self, bloodColor, points, damage, HP):
        self.bloodColor = bloodColor
        self.points = points
        self.damage = damage
        self.HP = HP
    def attack(self):
        att = random.randint(self.damage-10, self.damage+10) 

alien_0 = alienDefinition("green", 5, random.randint(20, 50), random.randint(300, 400))
alien_1 = alienDefinition("yellow", 10, random.randint(30, 60), random.randint(500, 600))
alien_2 = alienDefinition("blue", 15, random.randint(40, 70), random.randint(700, 800))
alien_3 = alienDefinition("red", 25, random.randint(70, 100), random.randint(1200, 1500))

print(alien_0.HP)
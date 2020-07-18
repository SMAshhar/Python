import csv

with open("priest.csv") as f:
    reader = csv.reader(f)
    priestly = []
    for a in reader:
        priestly += a
        print(priestly)

class WoWCharactor():
    def __init__(self, faction, race):
        self.faction = faction
        self.race = race

class Class(WoWCharactor):
    def __init__(self, faction, race, gender, Class):
        super().__init__(faction, race)
        self.gender = gender
        self.Class = Class

class Profession(Class):
    def __init__(self, faction, race, gender, Class, profession):
        super().__init__(faction, race, gender, Class)
        self.profession = profession

Elia = Profession("Alliance", "Night Elf", "Female", "Priest", "Herbalist")
level = 1

print(f'''Overview of Character
        Faction = {Elia.faction}
        Race = {Elia.race}
        Gender = {Elia.gender}
        Class = {Elia.Class}
        Profession = {Elia.profession}
        level = {level}
''')
powers = []

with open("priest.csv") as f:
    reader = csv.reader(f)
    for a in reader:
        powers += reader

x = 1        
for a in powers:
    print("Power", x, "=", a) 
    x += 1

input("Press any key to enter your World")

def smite(enemyHp):
    enemyHp -= (15 + level*30)
    print(enemyHp)
    return enemyHp

def shield(EliaHp):
    EliaHp += (5 + level*15)
    print(EliaHp)
    return EliaHp

def heal(EliaHp):
    EliaHp += (100 + level*50)
    print(EliaHp)
    return EliaHp

import random

input("You have been spotted by an enemy")
input("What will you do?")

enemyHp = random.randint(300, 700)
EliaHp = 500


while enemyHp > 0 and EliaHp > 0:
    action = input("Enter your command : ")
    if action.lower() == "smite":
        enemyHp = smite(enemyHp)
        EliaHp -= random.randint(50, 70)
    elif action.lower() == "shield":
        pass
    elif action.lower() == "heal":
        EliaHp = heal(EliaHp)
        EliaHp -= random.randint(50, 70)
    elif action.lower() == "none":
        EliaHp -= random.randint(50, 70)
    else:
        break
    
    print("Elia Hp = ", EliaHp)
    print("Enemy Hp = ", enemyHp)

if enemyHp <= 0:
    print("Victory")
elif EliaHp <= 0:
    print("You are dead, Game over")
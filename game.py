
class Warrior:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength



class Truncheon(Warrior):
    pass


class Bow(Warrior):
    def __init__(self, name, health, strength, distance, arrows):
        self.distance = 2
        self.arrows = 4


class Crossbow(Warrior):
    def __init__(self, distance):
        self.distance = 4


t1 = Truncheon("Ivan1", 30, 6)
b1 = Bow("Mihail1", 25, 4, 2, 4)
# c1 = Crossbow("Maxim1", 20, 5)


t2 = Truncheon("Ivan2", 30, 6)
b2 = Bow("Mihail2", 25, 4, 2, 4)
# c2 = Crossbow("Maxim2", 20, 5)

def attack(who, whom):
        whom.health -= who.strength



while True:
    attack(t1, t2)
    attack(b1, t2)
    print("У {} осталось жизней {}. У {} осталось жизней {}.".format(t1.name, t1.health, t2.name, t2.health))
    if t1.health <= 0 or t2.health <= 0:
      break
    attack(t2, t1)
    print("У {} осталось жизней {}. У {} осталось жизней {}.".format(t1.name, t1.health, t2.name, t2.health))
    if t1.health <= 0 or t2.health <= 0:
      break







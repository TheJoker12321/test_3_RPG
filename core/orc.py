import random
from core.monster import Monster



class Orc(Monster):
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.type = "Orc"
        self.speed = random.randint(0, 5)
        self.power = random.randint(10, 15)
        self.armor_rating = random.randint(2, 8)
        self.weapon = random.choice(["knife", "sword", "axe"])

    def speak(self):
        print(f"The {self.type} {self.name} is furious")

    def attack(self, opponent, game):
        result = self.speed + game.roll_dice(20)
        if opponent.armor_rating < result:
            if self.weapon == "knife":
                return (game.roll_dice(6) + self.power) * 0.5
            elif self.weapon == "sword":
                return (game.roll_dice(6) + self.power) * 1
            else:
                return (game.roll_dice(6) + self.power) * 1.5
        return "swap the turn"
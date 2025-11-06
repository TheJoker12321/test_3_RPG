import random
from core.monster import Monster



class Goblin(Monster):
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.type = "Goblin"
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = 1
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



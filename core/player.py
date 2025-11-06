import random


class Player:
    def __init__(self, name):
        self.name = name
        self.profession = random.choice(["Warrior", "Heal"])
        self.hp = 50 if self.profession == "Warrior" else 60
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10) if self.profession == "Heal" else random.randint(5, 10) + 2
        self.armor_rating = random.randint(5, 15)

    def speak(self):
        print(f"I am {self.name}")

    def attack(self, opponent, game):
        result = self.speed + game.roll_dice(20)
        if opponent.armor_rating < result:
            return game.roll_dice(6) + self.power
        return "swap the turn"





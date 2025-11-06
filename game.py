import random
from core.goblin import Goblin
from core.orc import Orc
from core.player import Player


class Game:
    @staticmethod
    def roll_dice(side):
        if side == 6:
            return random.randint(1, 6)
        elif side == 20:
            return random.randint(1, 20)
        else:
            raise AttributeError

    @staticmethod
    def choose_random_monster():
        return random.choice([Orc("Bob"), Goblin("John")])

    @staticmethod
    def show_menu():
        menu = input("""
______________________________________
choose "fight" if you want to fight 
or "exit" if you want to exit the game. 
______________________________________
""")
        while menu != "fight" and menu != "exit":
            menu = input("""
______________________________________
choose "fight" if you want to fight 
or "exit" if you want to exit the game. 
______________________________________
""")
        return menu

    def battle(self, player, monster):
        result_player = self.roll_dice(6) + player.speed
        result_monster = self.roll_dice(6) + monster.speed
        if result_player >= result_monster:
            print("player first.")
            while self.check_hp(monster) and self.check_hp(player):
                print("turn the player")
                player.speak()
                result = player.attack(monster, self)
                if result != "swap the turn":
                    monster.hp -= result
                print("turn the monster")
                monster.speak()
                result_mon = monster.attack(player, self)
                if result_mon != "swap the turn":
                    player.hp -= result_mon
        else:
            print("monster first.")
            while self.check_hp(player) and self.check_hp(monster):
                print("turn the monster")
                monster.speak()
                result_mon = monster.attack(player, self)
                if result_mon != "swap the turn":
                    player.hp -= result_mon
                print("turn the player")
                player.speak()
                result = player.attack(monster, self)
                if result != "swap the turn":
                    monster.hp -= result
        if not self.check_hp(monster):
            print("player won and monster dead")
        else:
            print("monster won and player dead")


    @staticmethod
    def check_hp(opponent) -> bool:
        if opponent.hp <= 0:
            return False
        return True


    def start(self):
        menu = self.show_menu()
        if menu == "exit":
            return
        monster = self.choose_random_monster()
        player = Player("Idan")
        self.battle(player, monster)



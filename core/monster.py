from abc import ABC, abstractmethod


class Monster(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def attack(self, opponent, game):
        pass

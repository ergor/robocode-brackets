
import random

class Round:
    def __init__(self, contestants, br_size):
        random.shuffle(contestants)
        self.__brackets = [Bracket(contestants[x:x+br_size]) \
                           for x in range(0, len(contestants), br_size)]

class Bracket:
    def set_winners(self, winners):
        self.__winners = winners

    def get_winners(self):
        return self.__winners

    def __init__(self, robots):
        self.__robots = robots
        self.__winners = []

"""
class Winner:
    def __init__(self):
        pass
"""

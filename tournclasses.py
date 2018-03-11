
import random

class Round:
    """
      Consists of multiple brackets
    """
    def __init__(self, contestants, br_size, roundno):
        self.__roundno = roundno
        random.shuffle(contestants)
        self.__brackets = [Bracket(contestants[x:x+br_size]) \
                           for x in range(0, len(contestants), br_size)]

    def get_no(self):
        return self.__roundno

    def get_brackets(self):
        return self.__brackets

    def get_winners(self):
        winners = [b.get_winners() for b in self.__brackets]
        return winners

    def print_robots(self):
        for bracket in self.__brackets:
            bracket.print_robots("  ")
            print("  ---")

class Bracket:
    """
        Consists of multiple robots
    """
    def __init__(self, robots):
        self.__robots = robots
        self.__winners = []

    def __len__(self):
        return len(self.__robots)

    def add_winner(self, winner):
        self.__winners.append(winner)

    def set_winners(self, winners):
        self.__winners = winners

    def get_winners(self):
        return self.__winners

    def print_robots(self, prestr="", poststr="\n"):
        for robot in self.__robots:
            print(prestr + robot, end=poststr)

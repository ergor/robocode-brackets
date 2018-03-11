
import pickle
from tournclasses import Round

from os import listdir
from os.path import isfile, join


"""
[ALL THE FOLLOWING ARE SUBJECT TO CHANGE: replaced by types.py?]
Round:      a list of brackets.
Bracket:    a list of contestants
Contestant: a robot .jar file strings
Winner:     a list of robot name, round and bracket number

Structure in file system:
- The manager read and writes data to the tournament directory. (whose name is
  an argument in the constructor of Manager)
- Each round is saved under the tournament directory as a pickle file with name
  "roundx" where x is the round number.
- To track which robots won which bracket for round x, a pickled winner object
  is saved in a subdirectory winnersx for each winner robot.
"""

class Manager:
    def get_roundname(self, roundno):
        return "round" + str(roundno)

    def get_roundno_max(self):
        return len(self.__rounds)

    # def select_round(self, num):
    #     if num <= self.__rounds and num > 0:
    #         self.__round = num
    #     else:
    #         print("error: round out of bounds")

    def get_round(self, roundno):
        return next((r for r in self.__rounds if r.get_no() == roundno), None)
        #return [self.__round, self.__rounds]

    def make_round(self, contestants, br_size):
        rnd = Round(contestants, br_size, self.get_roundno_max())

        file = join(self.__tournament, self.get_roundname(self.get_roundno_max()))
        with open(file, "wb") as fp:
            pickle.dump(rnd, fp)

        self.__rounds.append(rnd)

    def __init__(self, tournament):
        #self.__round = round_num
        #self.__rounds = rounds
        self.__tournament = tournament
        self.__rounds = []
        rounds = [f for f in listdir(tournament)
                  if isfile(join(tournament, f))
                  and f.startswith("round")]
        for file in rounds:
            with open(join(tournament, file), "rb") as fp:
                self.__rounds.append(pickle.load(fp))

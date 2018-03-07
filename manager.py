
from os import listdir, makedirs
from os.path import isfile, join, exists


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
    def select_round(self, num):
        if num <= self.__rounds and num > 0:
            self.__round = num
        else:
            print("error: round out of bounds")

    def get_round(self):
        # if round exists on fs, read and return.
        # otherwise, crate new, write to fs and return

        return [self.__round, self.__rounds]

    def __init__(self, tournament):
        pass
        #self.__round = round_num
        #self.__rounds = rounds
        self.__rounds = [f for f in listdir(tournament)
                            if isfile(join(tournament, f))
                            and f.startswith("round")]
        


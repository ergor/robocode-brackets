# robobr.py

import argparse
import random
import pickle
from os import listdir, makedirs
from os.path import isfile, join, exists

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("contestants", 
                            help="path to all contestant robot jars")
    parser.add_argument("-r", "--robocode", 
                            help="path to robocode directory",
                            metavar="PATH")
    parser.add_argument("-n", "--name",
                            help="the name of the tournament")
    args = parser.parse_args()
    if not exists(args.contestants):
        print("malformed argument: contestants: " \
              + "the given directory does not exist")
        exit()

    contestants = [f for f in listdir(args.contestants) 
                    if isfile(join(args.contestants, f))
                        and f.endswith(".jar")]
    tournament = "tournament" if args.name == None else args.name
    brackets = load_brackets(tournament, 1)
    if brackets == None:
        brackets = make_brackets(tournament, contestants, 4, 1)
        dump_brackets(tournament, 1, brackets)

    print(brackets)

def get_roundname(roundno):
    return "round" + str(roundno)

def load_brackets(tournament, roundno):
    file = join(tournament, get_roundname(roundno))
    if exists(file):
        with open(file, "rb") as fp:
            brackets = pickle.load(fp)
            return brackets
    else:
        return None

def dump_brackets(tournament, roundno, brackets):
    if not exists(tournament):
        makedirs(tournament)
    file = join(tournament, get_roundname(roundno))
    with open(file, "wb") as fp:
        pickle.dump(brackets, fp)

def make_brackets(tournament, contestants, br_size, roundno):
    random.shuffle(contestants)
    brackets = [contestants[x:x+br_size] \
                for x in range(0, len(contestants), br_size)]
    return brackets

main()
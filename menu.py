
#from manager import Manager
#from rt_types import Round

def menu(manager):
    menu_round(manager.get_round(0))

def menu_round(round_obj):
    roundno = round_obj.get_no()
    brackets = round_obj.get_brackets()
    def print_menu():
        print("[MENU OPTIONS]\n" \
            + "pr    : print all robots in this round\n" \
            + "p <n> : print stats for bracket n\n" \
            + "r <n> : jump to round n\n" \
            + "g     : go! starts interactive walkthrough of each bracket\n" \
            + "q     : quit program\n" \
            + "<else>: print this menu + stats summary\n")
        print("[ROUND STATS]")
        print("brackets: " + str(len(brackets)))
        print("robots:   " + str(sum(map(len, brackets))))
    print_menu()
    print("")
    in_str = ""
    while in_str != "q":
        in_str = input("round " + str(roundno) + "> ")
        print("")
        if in_str == "pr":
            ## TODO: for each bracket, if winners are selected, mark as such
            round_obj.print_robots()
        elif in_str.startswith("p "):
            pass
        elif in_str.startswith("r "):
            pass
        elif in_str == "g":
            menu_bracket(roundno, brackets)
        else:
            print_menu()
        print("")

def menu_bracket(rnd, brackets):
    print("[MENU OPTIONS]\nn : go to next bracket\n" \
                        + "q : quit to round menu")

    for i in range(len(brackets)):
        print("\n[BRACKET STATS]")
        for robot in brackets[i]:
            print("  " + robot)
        print("")

        in_str = ""
        while(in_str != "q" and in_str != "n"):
            in_str = input("bracket " + str(i+1) + " @" + str(rnd) + "> ")

        if in_str == "n":
            i += 1
        else:
            return


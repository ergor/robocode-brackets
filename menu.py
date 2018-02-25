

def menu(rnd, brackets):
    print("[MENU OPTIONS]\npr   : print all robots in this round\n" \
                        + "p <n>: print robots in bracket n\n" \
                        + "r <n>: jump to round n\n" \
                        + "g    : go! starts interactive walkthrough of each" \
                        +        " bracket\n" \
                        + "q    : quit program and save tournament\n")
    print("[ROUND STATS]")
    print("brackets: " + str(len(brackets)))
    print("robots:   " + str(sum(map(len, brackets))) + "\n")
    menu_round(rnd, brackets)

def menu_round(rnd, brackets):
    in_str = ""
    while(in_str != "q"):
        in_str = input("round " + str(rnd) + "> ")
        if in_str == "pr":
            for bracket in brackets:
                for robot in bracket:
                    print("  " + robot)
                print("  ---")
        elif in_str.startswith("p "):
            pass
        elif in_str.startswith("r "):
            pass
        elif in_str == "g":
            menu_bracket(rnd, brackets)

def menu_bracket(rnd, brackets):
    print("[MENU OPTIONS]\nn : save and go to next bracket\n" \
                        + "q : quit to round menu")
    i = 0
    for i in range(len(brackets)):
        print("\n[BRACKET]")
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


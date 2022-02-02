#By Alex Zhu
# is this really what I do with my freetime?

import random

if __name__ == "__main__":
    #read word list, get a random solution
    wlst = open("wordle_list.txt",'r').readlines()
    solution = wlst[random.randint(0,len(wlst)-1)]

    #print(solution) #you can uncomment this if you want to cheat or bugtest

    #initialize game-play loop
    win = False
    guessCount = 0
    print("WORDLE BY ALEX\n _ = wrong | ? = letter in wrong place | \u2713 = letter in right place")
    while (not win and guessCount < 7):
        #take user guess
        guess = input()

        #check guess against solution
        out_str = ""
        for i in range(len(guess)):
            if guess[i] == solution[i]:
                out_str += "\u2713"
            elif guess[i] in solution:
                out_str += "?"
            else:
                out_str += "_"

        guessCount += 1
        print(out_str)

        #check win condition
        win = (out_str == "\u2713"*5)
    
    #display win messages
    if win:
        print("\nYou won in {0} guesses!".format(guessCount))
    else:
        print("\nYou lose, loser. The solution was: {0}".format(solution))

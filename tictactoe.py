# holding
board = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}

# checking if it is a number
aloud = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# checking if it used
used = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# just for later to check if 'used' if full
empty = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# makes the board
def showBoard():
    print(board["1"] + "||" + board["2"] + "||" + board["3"])
    print("=======")
    print(board["4"] + "||" + board["5"] + "||" + board["6"])
    print("=======")
    print(board["7"] + "||" + board["8"] + "||" + board["9"])
    print("\n")


player1turn = True

gameBool = True

# lets you play
def playerTurn():
    global player1turn
    if player1turn:
        if spot == "1":
            board["1"] = 'x'
            used[0] = "-"
        elif spot == "2":
            board["2"] = 'x'
            used[1] = "-"
        elif spot == "3":
            board["3"] = 'x'
            used[2] = "-"
        elif spot == "4":
            board["4"] = 'x'
            used[3] = "-"
        elif spot == "5":
            board["5"] = 'x'
            used[4] = "-"
        elif spot == "6":
            board["6"] = 'x'
            used[5] = "-"
        elif spot == "7":
            board["7"] = 'x'
            used[6] = "-"
        elif spot == "8":
            board["8"] = 'x'
            used[7] = "-"
        elif spot == "9":
            board["9"] = 'x'
            used[8] = "-"
        player1turn = False
    else:
        if spot == "1":
            board["1"] = 'o'
            used[0] = "-"
        elif spot == "2":
            board["2"] = 'o'
            used[1] = "-"
        elif spot == "3":
            board["3"] = 'o'
            used[2] = "-"
        elif spot == "4":
            board["4"] = 'o'
            used[3] = "-"
        elif spot == "5":
            board["5"] = 'o'
            used[4] = "-"
        elif spot == "6":
            board["6"] = 'o'
            used[5] = "-"
        elif spot == "7":
            board["7"] = 'o'
            used[6] = "-"
        elif spot == "8":
            board["8"] = 'o'
            used[7] = "-"
        elif spot == "9":
            board["9"] = 'o'
            used[8] = "-"
        player1turn = True

# checks for a win or draw
def win():
    global gameBool
    if board["1"] == board["2"] == board["3"] and board["1"] == "x":
        gameBool = False
        print("X wins!")
        # x wins
    elif board["4"] == board["5"] == board ["6"] and board["4"] == "x":
        gameBool = False
        print("X wins!")
    elif board["7"] == board["8"] == board ["9"] and board["7"] == "x":
        gameBool = False
        print("X wins!")
    elif board["1"] == board["4"] == board ["7"] and board["1"] == "x":
        gameBool = False
        print("X wins!")
    elif board["2"] == board["5"] == board ["8"] and board["2"] == "x":
        gameBool = False
        print("X wins!")
    elif board["3"] == board["6"] == board ["9"] and board["3"] == "x":
        gameBool = False
        print("X wins!")
    elif board["1"] == board["5"] == board ["9"] and board["1"] == "x":
        gameBool = False
        print("X wins!")
    elif board["3"] == board["5"] == board ["7"] and board["7"] == "x":
        gameBool = False
        print("X wins!")
    # check for o wins
    elif board["1"] == board["2"] == board["3"] and board["1"] == "o":
        gameBool = False
        print("O wins!")
        # o wins
    elif board["4"] == board["5"] == board ["6"] and board["4"] == "o":
        gameBool = False
        print("O wins!")
    elif board["7"] == board["8"] == board ["9"] and board["7"] == "o":
        gameBool = False
        print("O wins!")
    elif board["1"] == board["4"] == board ["7"] and board["1"] == "o":
        gameBool = False
        print("O wins!")
    elif board["2"] == board["5"] == board ["8"] and board["2"] == "o":
        gameBool = False
        print("O wins!")
    elif board["3"] == board["6"] == board ["9"] and board["3"] == "o":
        gameBool = False
        print("O wins!")
    elif board["1"] == board["5"] == board ["9"] and board["1"] == "o":
        gameBool = False
        print("O wins!")
    elif board["3"] == board["5"] == board ["7"] and board["7"] == "o":
        gameBool = False
        print("O wins!")
    # draw
    elif used == empty:
        gameBool = False
        print("Draw!")
    else:
        pass

# Introduction
print("Welcome to tic-tac-toe by willow. X, you go first")
# the game while loop
while gameBool:
    showBoard()
    # check if the spot is taken and if its a number
    spot = input("Where do you want to go? (1-9): ")
    if spot in aloud and spot in used:
        playerTurn()
    else:
        print("That was not a number from 1 to 9 or someone has already moved there, please try again")
        pass
    # check for x wins
    win()

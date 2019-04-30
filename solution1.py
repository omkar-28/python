import random
user = 0
comp = 0
moves = ['rock','paper','scissor']
moves_pref = [0,1,2]

def play():
    global user
    global comp
    user_move = input("Rock, Paper, Scissor? ")
    try:
        user_move = moves_pref[(moves.index(user_move))]
        comp_move = random.choice(moves_pref)
    except ValueError:
        print("Please type only Rpck, Paper, Scissor")
        return 1

    print("my Move: ",moves[comp_move])
    if(user_move == comp_move):
        print("It's a tie")
    elif(user_move == 0 and comp_move == 2):
        print("YOU WIN")
        user += 1
    elif(user_move == 1 and comp_move == 0):
        print("YOU WIN")
        user += 1
    elif(user_move == 2 and comp_move == 1):
        print("YOU WIN")
        user += 1
    else:
        print("I WIN")
        comp += 1

counter = 'y'
while True:
    if(counter == 'score'):
        print("the score is\n{a}\t{b}\n{:^4}\t{:^7}".format(str(user), str(comp),a="USER",b="COMPUTER"))
        counter = input("Do you want to play again? (Y/N) ")
    if(counter == 'N' or counter == 'n'):
        print("Thanks for playing")
        break
    elif(counter == 'Y' or counter == 'y'):
        play()
        counter = input("Do you want to play again? (Y/N) \nType score anytime to check the score\n")
    print('\n')
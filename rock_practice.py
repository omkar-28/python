import random
user = 0
comp = 0
moves = ["rock","paper","scissor"]
moves_pref = [0,1,2]

def play():
    global user
    global comp
    user_moves = input("rock, paper, scissor? ")
    try:
        user_moves = moves_pref[moves.index(user_moves)]
        comp_moves = random.choice(moves_pref)
    except ValueError:
        print("Please type only rock, paper, scissor")
        return 1

    print("My moves", moves[comp_moves])
    if (user_moves == comp_moves):
        print("it's a tie")
    elif(user_moves == 0 and comp_moves == 2):
        user +=1
        print("You win")
    elif(user_moves == 1 and comp_moves == 0):
        user +=1
        print("You win")
    elif(user_moves == 2 and comp_moves == 1):
        user +=1
        print("You win")
    else:
        comp +=1
        print("I won")

counter = "y"
while True:
    if(counter == 'score'):
        print("The score is\nYOU\tME\n"+str(user)+"\t"+str(comp))
        counter = input("Do you want to play again? (Y/N): ")
    if(counter =="n" or counter =="N"):
        print("\nthank you for playing!!.")
        break
    elif(counter == "y" or counter =="Y"):
        play()
        counter = input("Do you want to play again? (Y/N)\nYou can check scorre at anytime by typing score. \n")
    print('\n\n')

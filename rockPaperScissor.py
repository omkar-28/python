# #import randit 
# from random import randint

# #take the input for users
# game_over = False
    
# while not game_over:

#     player = input("Please select \nrock(r), paper (p) or scissors(s)? ")
#     print(player,'vs', end=" ")
#     choose = randint(1,3)
#     if choose == 1:
#         computer = "r"
#     elif choose == 2:
#         computer = "p"
#     else:
#         computer = "s"
#     print(computer)

#     if player == computer:
#         print("Draw")

#     elif player =="r" and computer == "p":
#         print("computer won")
#     elif player == "r" and computer =="s":
#         print("Player won")
#     elif player =="p" and computer == "r":
#         print("Player won")
#     elif player == "p" and computer =="s":
#         print("computer won")
#     elif player =="s" and computer == "p":
#         print("Player won")
#     elif player == "s" and computer =="r":
#         print("computer won")

#     player = input('Would you like to play again? ')
# print('Thank you for playing.')

# from random import randint

# def play_game():
#     print("Rock Paper Scissors game")

#     rps = ['rock','paper','scissor']
#     player = input("Choose Rock, Paper, Scissor").casefold()
#     computer = random.choice(rps)

#     if player == "rock":
#         if computer == "rock":
#             print(f"{player} vs {computer} : Tie")
#         elif computer == "paper":
#             print(f"{player} vs {computer} : You Loose")
#         elif computer == "scissor":
#             print(f"{player} vs {computer} : You Win")

#     if player == "paper":
#         if computer == "rock":
#             print(f"{player} vs {computer} : You Win")
#         elif computer == "paper":
#             print(f"{player} vs {computer} : Tie")
#         elif computer == "scissor":
#             print(f"{player} vs {computer} : You Loose")

#     if player == "scissor":
#         if computer == "rock":
#             print(f"{player} vs {computer} : You Loose")
#         elif computer == "paper":
#             print(f"{player} vs {computer} : You Win")
#         elif computer == "scissor":
#             print(f"{player} vs {computer} : Tie")

#     play_game = input("Play gaian? ").casefold()
#     if play_game == "yes" or play_game == "y":
#         play_game()
#     else:
#         print("Game Over!!. \nThanks for playing")

# play_game()
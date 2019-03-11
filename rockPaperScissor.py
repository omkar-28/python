#import randit 
from random import randint

#take the input for users
player = input("Please select \nrock(r), paper (p) or scissors(s)? ")
print(player,'vs', end=" ")

choose = randint(1,3)
if choose == 1:
    computer = "r"
elif choose == 2:
    computer = "p"
else:
    computer = "s"
print(computer)

if player == computer:
    print("Draw")
elif player =="r" and computer == "p":
    print("computer won")
elif player == "r" and computer =="s":
    print("Player won")
elif player =="p" and computer == "r":
    print("Player won")
elif player == "p" and computer =="s":
    print("computer won")
elif player =="s" and computer == "p":
    print("Player won")
elif player == "s" and computer =="r":
    print("computer won")
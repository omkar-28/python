from random import randint

roll = "yes"

while roll =="yes" or roll =="y":
    print("the dice is rolling...")
    print("The number is",randint(1,6))

    roll = input("do you want to roll again?")
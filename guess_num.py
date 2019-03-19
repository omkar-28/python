import random
win_num = random.randint(1,100)
print(win_num)
guess = 1
user_num = int(input("Guiess the number between  1 to 100: " ))
game_over = False

while not game_over:
    if user_num == win_num:
        print("YOu won, and you guees the number in {} times".format(guess))
        game_over =True
    else:
        if user_num < win_num:
            print("Too low")
        else: 
            print("Too High")
        guess +=1
        user_num = int(input("Guess again: "))
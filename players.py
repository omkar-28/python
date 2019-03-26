from random import choice

players = ["Dhoni","Virat","Rohit","Dhawan","Rahul","Pant","Bhuvaneshwar","Kedar"]
print(players)

teamA=[]
teamB=[]

while len(players) > 0:
    playerA=choice(players)
    teamA.append(playerA)
    players.remove(playerA)

    if players==[]:
        break

    playerB=choice(players)
    teamB.append(playerB)
    players.remove(playerB)
    
print("teamA:",teamA)
# print("teamB:",teamB)
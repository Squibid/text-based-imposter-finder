import random

maxPlayers = 5
alivePlayers = maxPlayers
SUS_nums = []

while alivePlayers > 1:
    player1 = random.randint(1, maxPlayers)
    SUS_nums.append(player1)
    player2 = random.randint(1, maxPlayers)
    while player2 in SUS_nums:
        player2 = random.randint(1, maxPlayers)
    SUS_nums.append(player2)
    player3 = random.randint(1, maxPlayers)
    while player3 in SUS_nums:
        player3 = random.randint(1, maxPlayers)
    SUS_nums.append(player3)
    player4 = random.randint(1, maxPlayers)
    while player4 in SUS_nums:
        player4 = random.randint(1, maxPlayers)
    SUS_nums.append(player4)
    player5 = random.randint(1, maxPlayers)
    while player5 in SUS_nums:
        player5 = random.randint(1, maxPlayers)
    SUS_nums.append(player5)

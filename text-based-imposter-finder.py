from asyncio import tasks
import random, os, time, pygame, sys
pygame.init()
pygame.mixer.init()

class Color:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    END = '\033[0m'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def room_spawn(room_spawn):
    room_spawn = random.randint(1, len(rooms))
    while room_spawn == 2 or room_spawn == 3:
        room_spawn = random.randint(1, len(rooms))
    p_room = room_spawn - 1
    return p_room

def AI_moving(p_roome):
    if random.randint(1, 2) != 1:
        if p_roome == 0:
            p_roome = 1
        elif p_roome == 1:
            buckets = random.randint(0, 3)
            if buckets == 0:
                p_roome = 0
            elif buckets == 1:
                p_roome = 2
            elif buckets == 2:
                p_roome = 3
            elif buckets == 4:
                p_roome = 4
        elif p_roome == 2:
            buckets = random.randint(0, 2)
            if buckets == 0:
                p_roome = 1
            elif buckets == 1:
                p_roome = 5
            elif buckets == 2:
                p_roome = 6
        elif p_roome == 3 or p_roome == 4:
            p_roome = 1
        elif p_roome == 5 or p_roome == 6:
            p_roome = 2
    return p_roome
task1Complete = False
task2Complete = False
task3Complete = False
task4Complete = False
task5Complete = False

def task1(): #task 1 in Meeting Room
    clear()
    HUD()
    print("Task: Refill the water cooler\n")
    if task1Complete == True:
        print("Task Already Complete")
        time.sleep(2)
    while task1Complete != True:
        task1p1 = input("unscrew bottle ")
        if task1p1 == 'unscrew':
            task1p2 = input("flip bottle ")
            if task1p2 == 'flip':
                task1p3 = input("replace bottle ")
                if task1p3 == 'replace':
                    task1p4 = input("screw in new bottle ")
        if task1p1 == 'unscrew' and task1p2 == 'flip' and task1p3 == 'replace' and task1p4 == 'screw':
            print("task completed sucessfully!")
            task1Complete = True
        else:
            print("task failed try again")

def task2(): #task 2 in Gift Card Center
    clear()
    HUD()
    print("Task: Give John Wick the 16 numbers on the front of your moms credit card and the 4 on the back!")
    task2Complete = False
    if task2Complete == True:
        print("Task Already Complete")

def task3(): #task 3 in Mart
    clear()
    HUD()
    print("Task: Buy a pen, pineapple, apple, pen")
    task3Complete = False
    if task3Complete == True:
        print("Task Already Complete")

def task4(): #task 4 Room of Stuff
    clear()
    HUD()
    print("Task: Find the correct stuff")
    task4Complete = False
    if task4Complete == True:
        print("Task Already Complete")

def task5(): #task 5 Lamp Making Room
    clear()
    HUD()
    print("Task: Make a lamp")
    task5Complete = False
    if task5Complete == True:
        print("Task Already Complete")

max_players = 5
rooms = ["Meeting Room", "Hallway 1", "Hallway 2", "Gift Card Center", "Room Of Stuff", "Mart", "Lamp Making Room"]
tasks = ["Water Cooler", "John Wick", "3", "4", "5",]
SUS_nums = []
alive_players = max_players
p_sus = 0
p1_room = 0
p2_room = 0
p3_room = 0
p4_room = 0
p5_room = 0
AI_boz = 0

# idk tbh - a morman *HOLY NOISES INTENSIF*
player1 = random.randint(1, max_players)
SUS_nums.append(player1)
player2 = random.randint(1, max_players)
while player2 in SUS_nums:
    player2 = random.randint(1, max_players)
SUS_nums.append(player2)
player3 = random.randint(1, max_players)
while player3 in SUS_nums:
    player3 = random.randint(1, max_players)
SUS_nums.append(player3)
player4 = random.randint(1, max_players)
while player4 in SUS_nums:
    player4 = random.randint(1, max_players)
SUS_nums.append(player4)
player5 = random.randint(1, max_players)
while player5 in SUS_nums:
    player5 = random.randint(1, max_players)
SUS_nums.append(player5)
sus = random.randint(1, max_players)

NPC_movent = False
debug_map = False
start = False
while start == False:
    clear()
    print("Welcome to text based imposter finder!")
    print("(1) start game")
    print("(2) settings")
    menu_input = int(input("Enter a number for what action you want to do: "))
    if menu_input == 1:
        start = True
    if menu_input == 2:
        clear()
        print("(1) Enable debug map")
        print("(2) Enable NPC movement data")
        menu_input = int(input("Enter a number for what action you want to do: "))
        if menu_input == 1:
            debug_map = True
        if menu_input == 2:
            NPC_movent = True

# check if you are imposter
clear()
if player1 == sus:
    print(Color.RED + "You are the imposter" + Color.END)
    p_sus = 1
else:
    print(Color.BLUE + "You are a crewmate" + Color.END)
    
rp1t1 = random.randint(0, 4)
rp1t2 = random.randint(0, 4)
if rp1t1 == rp1t2:
    rp1t2 += 1
    if rp1t2 > 4:
        rp1t2 = 0

def HUD():
    if debug_map == True:
        print(" _______ ")
        print("|   0   |")
        print("|__| |__|")
        print("|3  1  4|")
        print("|__| |__|")
        print("|5  2  6|")
        print("|__|_|__|")
    if p_sus == 1:
        print(Color.BOLD + "Role:" + Color.END + Color.RED, "Imposter" + Color.END)
    else:
        print(Color.BOLD + "Role:" + Color.END + Color.BLUE, "Crewmate" + Color.END)
    print(Color.BOLD + "Current Room: " + Color.END + rooms[p1_room])
    if p1_room == p2_room or p1_room == p3_room or p1_room == p4_room or p1_room == p5_room:
        sys.stdout.write(Color.BOLD + "In room: " + Color.END)
    if p1_room != p2_room and p1_room != p3_room and p1_room != p4_room and p1_room != p5_room:
        print(Color.BOLD + "In room: " + Color.END)
    if p1_room == p2_room:
        sys.stdout.write("???2 ")
    if p1_room == p3_room:
        sys.stdout.write("???3 ")
    if p1_room == p4_room:
        sys.stdout.write("???4 ")
    if p1_room == p5_room:
        sys.stdout.write("???5")
    if p1_room == p2_room or p1_room == p3_room or p1_room == p4_room or p1_room == p5_room:
        sys.stdout.write('\n')
    print(Color.BOLD + "Task #1: " + Color.END + tasks[rp1t1])
    print(Color.BOLD + "Task #2: " + Color.END + tasks[rp1t2], '\n') 

susMusic = pygame.mixer.Sound('sus.wav')
susMusic.play()
time.sleep(3)

#check if a cpu is sus
if player2 == sus:
    p_sus = 2
elif player3 == sus:
    p_sus = 3
elif player4 == sus:
    p_sus = 4
elif player5 == sus:
    p_sus = 5

#room spawn for everybody(as a millionaire)
p1_room = room_spawn(p1_room)
p2_room = room_spawn(p2_room)
p3_room = room_spawn(p3_room)
p4_room = room_spawn(p4_room)
p5_room = room_spawn(p5_room)


# != GIGA GENIUS MOVEMENT CODE
while True:
    clear()
    if p1_room == 0:
        HUD()
        if rp1t1 != 0 or rp1t2 != 0:
            print("(1) Move into Hallway 1 ")
        if rp1t1 == 0 or rp1t2 == 0:
            print("(2)", tasks[0], "task")
        move_input = int(input("Enter a number for what action you want to do: "))
        if move_input == 1:
            p1_room = 1
            AI_boz = 1
        elif move_input == 2 and (rp1t1 == 0 or rp1t2 == 0):
            task1()
            AI_boz = 1
    elif p1_room == 1:
        HUD()
        print("(1) Move into Hallway 2 \n(2) Move into Gift Card Center \n(3) Move into Room Of Stuff \n(4) Move into Meeting Room")
        move_input = int(input("Enter a number for what action you want to do: "))
        if move_input == 1:
            p1_room = 2
            AI_boz = 1
        elif move_input == 2:
            p1_room = 3
            AI_boz = 1
        elif move_input == 3:
            p1_room = 4
            AI_boz = 1
        elif move_input == 4:
            p1_room = 0
            AI_boz = 1
    elif p1_room == 2:
        HUD()
        print("(1) Move into Hallway 1 \n(2) Move into Mart \n(3) Move into Lamp Making Room")
        move_input = int(input("Enter a number for what action you want to do: "))
        if move_input == 1:
            p1_room = 1
            AI_boz = 1
        elif move_input == 2:
            p1_room = 5
            AI_boz = 1
        elif move_input == 3:
            p1_room = 6
            AI_boz = 1
    elif p1_room == 3:
        HUD()
        print("(1) Move into Hallway 1 ")
        move_input = int(input("Enter a number for what action you want to do: "))
        if move_input == 1:
            p1_room = 1
            AI_boz = 1
    elif p1_room == 4:
        HUD()
        print("(1) Move into Hallway 1 ")
        move_input = int(input("Enter a number for what action you want to do: "))
        if move_input == 1:
            p1_room = 1
            AI_boz = 1
    elif p1_room == 5:
        HUD()
        print("(1) Move into Hallway 2 ")
        move_input = int(input("Enter a number for what action you want to do: "))
        if move_input == 1:
            p1_room = 2
            AI_boz = 1
    elif p1_room == 6:
        HUD()
        print("(1) Move into Hallway 2 ")
        move_input = int(input("Enter a number for what action you want to do: "))
        if move_input == 1:
            p1_room = 2
            AI_boz = 1
            
    if AI_boz == 1:
        t = AI_moving(p2_room)
        if NPC_movent == True:
            print("p2 room", t)
        tt = AI_moving(p3_room)
        if NPC_movent == True:
            print("p3 room", tt)
        ttt = AI_moving(p4_room)
        if NPC_movent == True:
            print("p4 room", ttt)
        tttt = AI_moving(p5_room)
        if NPC_movent == True:
            print("p5 room", tttt)
        AI_boz = 0
        if NPC_movent == True:
            time.sleep(2)

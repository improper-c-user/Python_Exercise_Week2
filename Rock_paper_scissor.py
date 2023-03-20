from random import randint
game_state = True

print("Jan, Ken, Pong ")
while game_state is True:
    player_input = int(input("Chose:\n1.Rock\n2.Paper\n3.Scissors\nInput:"))
    if player_input > 3 or player_input < 1:
        print("\t\tinvalid input")
        continue
    comp = randint(1,3)
    print("\t\tComp choice:", comp)
    if player_input == comp:
        print("Let go again :)")
        continue
    elif player_input != comp:
        if (player_input == 1 and comp == 2) or (player_input == 2 and comp == 3) or (player_input == 3 and comp == 1):
            print("\t\tToo bad, try again Next time Loser :>")
            game_state = False
        else:
            print("\t\tPlayer wins >:<")
            game_state = False



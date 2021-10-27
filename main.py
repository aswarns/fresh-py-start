

print("welcome to the GAME")
player = input("to play either press right or left\n....")
player = player.lower()

if player == "right" or player == "r":
    print("\ngoing to right direction , u will see SEA soon")
    player = input("to play either press right or left\n....")
    player = player.lower()
    if player == "right" or player == "r":
        print("going to right direction , u will see CAR soon")
        player = input("to play either press right or left\n....")
        player = player.lower()
        if player == "right" or player == "r":
            print("going to right direction , u will see TV soon")
            print("WOOOOOOOOOOON")
        elif player == "left" or player == 'l':
            print("GOING NO WHERE, GAME OVER")
        else:
            print("GAME OVEEEEEEEEEER")
    else:
        print("GAME OVER, u fell in SEA")
else:
    print("GAME OVER, u fell in SEA")




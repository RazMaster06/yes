total = 21
is_player_one = True

while total >= 0:
    if is_player_one == True:
        print("Hur mycket vill du ta bort Player 1? 1-5")
    else:
        print("Hur mycket vill du ta bort Player 2? 1-5")
    amount = int(input())
    total -= amount
    if total < 1:
        if is_player_one == True:
            print("Du vann Player 2")
            break
        else:
            print("Du vann Player 1")
            break
    print("Det finns", total, "kvar")
    is_player_one = not is_player_one